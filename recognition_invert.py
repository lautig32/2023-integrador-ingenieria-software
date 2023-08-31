import cv2
import face_recognition

def recognition(image_list):

    recognized_faces = []

    # Cargar las imágenes de las personas de interés
    imagenes_personas_interes = [face_recognition.load_image_file(image_file) for image_file in image_list]
    encodings_personas_interes = [face_recognition.face_encodings(imagen_persona)[0] for imagen_persona in imagenes_personas_interes]

    # Cargar las imágenes objetivo individuales
    imagenes_objetivo = [
        face_recognition.load_image_file('IMG_2011.jpeg'),
    ]

    for imagen_objetivo in imagenes_objetivo:
        imagen_objetivo_copy = imagen_objetivo.copy()
        
        rostros_objetivo = face_recognition.face_locations(imagen_objetivo)
        
        for rostro_objetivo in rostros_objetivo:
            imagen_objetivo_encodings = face_recognition.face_encodings(imagen_objetivo, [rostro_objetivo])[0]
            face_recognized = False

            for encoding_persona_interes in encodings_personas_interes:
                resultado = face_recognition.compare_faces([encoding_persona_interes], imagen_objetivo_encodings)[0]
                if resultado:
                    recognized_faces.append(rostro_objetivo)
                    top, right, bottom, left = rostro_objetivo
                    cv2.rectangle(imagen_objetivo_copy, (left, top), (right, bottom), (0, 255, 0), 2)
                    face_recognized = True

            if not face_recognized:
                top, right, bottom, left = rostro_objetivo
                cv2.rectangle(imagen_objetivo_copy, (left, top), (right, bottom), (0, 0, 255), 2)

        # # Mostrar la imagen objetivo con los cuadros
        # # Crear la ventana con el nombre 'Reconocimiento facial'
        # cv2.namedWindow('Reconocimiento facial', cv2.WINDOW_NORMAL)
        # # Cambiar las dimensiones de la ventana
        # cv2.resizeWindow('Reconocimiento facial', 800, 600)
        
        # cv2.imshow('Reconocimiento facial', imagen_objetivo_copy)
        # cv2.waitKey(0)
        
        # Guardar una copia de la imagen con los cuadros dibujados
        cv2.imwrite('imagen_objetivo_con_cuadros.jpg', imagen_objetivo_copy)

    return recognized_faces

# Lista de imágenes a rastrear
imagenes_a_rastrear = [
    # "Lautaro.jpg", 
    "Sofia.jpg"
]

# Llamar a la función recognition con la lista de imágenes a rastrear
recognized_faces = recognition(imagenes_a_rastrear)

# Imprimir las ubicaciones de las caras reconocidas
print("Ubicaciones de las caras reconocidas:", recognized_faces)

cv2.destroyAllWindows()  # Cerrar todas las ventanas de OpenCV al final
