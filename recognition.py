import cv2
import face_recognition

def recognition(image_person):

    recognized_faces = []


    imagen_persona = face_recognition.load_image_file(image_person)
        
    face_locations = face_recognition.face_locations(imagen_persona)

    if len(face_locations) > 0:
        imagen_persona_encodings = face_recognition.face_encodings(imagen_persona, face_locations)[0]

    # Cargar la imagen objetivo
    imagen_objetivo = face_recognition.load_image_file('IMG_0562.jpeg')
    rostros_objetivo = face_recognition.face_locations(imagen_objetivo)

    print(len(rostros_objetivo))


    # Recorrer los rostros detectados en la imagen objetivo
    for rostro_objetivo in rostros_objetivo:
        # Extraer las características faciales del rostro objetivo
        imagen_objetivo_encodings = face_recognition.face_encodings(imagen_objetivo, [rostro_objetivo])[0]

        # Comparar el rostro objetivo con la imagen de la persona de interés
        resultado = face_recognition.compare_faces([imagen_persona_encodings], imagen_objetivo_encodings)[0]
        if resultado:
            # Si se encontró una coincidencia, hacer algo con el resultado
            # por ejemplo, resaltar el rostro o mostrar una identificación
            top, right, bottom, left = rostro_objetivo
            cv2.rectangle(imagen_objetivo, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(imagen_objetivo, 'Persona de interés', (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Crear la ventana con el nombre 'Reconocimiento facial'
    cv2.namedWindow('Reconocimiento facial', cv2.WINDOW_NORMAL)
    # Cambiar las dimensiones de la ventana
    cv2.resizeWindow('Reconocimiento facial', 800, 600)

    # Mostrar la imagen objetivo con los resultados
    cv2.imshow('Reconocimiento facial', imagen_objetivo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cargar la imagen de la persona de interés
recognition('Lautaro.jpg')
# recognition('Sofia.jpg')