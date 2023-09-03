import cv2
import face_recognition
import os

class FaceRecognition:
    def __init__(self, image_list):
        self.image_list = image_list
        self.encodings_personas_interes = []
        self.load_person_images()

    def load_person_images(self):
        base_dir = os.path.dirname(__file__)  # Get the base directory path
        # Load images of the persons of interest
        self.imagenes_personas_interes = [face_recognition.load_image_file(os.path.join(base_dir, image_file)) for image_file in self.image_list]
        self.encodings_personas_interes = [face_recognition.face_encodings(imagen_persona)[0] for imagen_persona in self.imagenes_personas_interes]

    def recognize_faces(self, imagen_objetivo_path):
        base_dir = os.path.dirname(__file__)  # Get the base directory path
        # Load the target image
        imagen_objetivo = cv2.imread(os.path.join(base_dir, imagen_objetivo_path))
        imagen_objetivo_copy = imagen_objetivo.copy()

        # Find face locations in the target image
        rostros_objetivo = face_recognition.face_locations(imagen_objetivo)

        for rostro_objetivo in rostros_objetivo:
            imagen_objetivo_encodings = face_recognition.face_encodings(imagen_objetivo, [rostro_objetivo])[0]
            face_recognized = False

            for encoding_persona_interes in self.encodings_personas_interes:
                resultado = face_recognition.compare_faces([encoding_persona_interes], imagen_objetivo_encodings)[0]
                if resultado:
                    top, right, bottom, left = rostro_objetivo
                    cv2.rectangle(imagen_objetivo_copy, (left, top), (right, bottom), (0, 255, 0), 2)
                    face_recognized = True

            if not face_recognized:
                top, right, bottom, left = rostro_objetivo
                cv2.rectangle(imagen_objetivo_copy, (left, top), (right, bottom), (0, 0, 255), 2)

        return imagen_objetivo_copy

base_dir = os.path.dirname(os.path.dirname(__file__))
"/Users/nexo.lgomez/personal-project/IntegradorIngenieriaSoftware/apps"
print(base_dir)
"media/players/47477067-BCAC-427A-B51D-BB1528CE0EC6.jpeg"

base_dir = os.path.dirname(__file__)

# List of images to search for faces
imagenes_a_rastrear = [
    "lautaro.jpg"
]

# Initialize the FaceRecognition class with the list of images
face_recognition_obj = FaceRecognition(imagenes_a_rastrear)

# Path to the target image
imagen_objetivo_path = "buscamos.jpg"

# Call the recognize_faces method to find and highlight faces in the target image
result_image = face_recognition_obj.recognize_faces(imagen_objetivo_path)

# Save the final image with highlighted faces
cv2.imwrite(os.path.join(base_dir, 'imagen_objetivo_con_cuadros.jpg'), result_image)


#######


import cv2
import face_recognition

def recognition(image_list):

    recognized_faces = []

    # Cargar las imágenes de las personas de interés
    imagenes_personas_interes = [face_recognition.load_image_file(image_file) for image_file in image_list]
    encodings_personas_interes = [face_recognition.face_encodings(imagen_persona)[0] for imagen_persona in imagenes_personas_interes]

    # Cargar las imágenes objetivo individuales
    imagenes_objetivo = [
        face_recognition.load_image_file('buscamos.jpg'),
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
    "lautaro.jpg"
]

# Llamar a la función recognition con la lista de imágenes a rastrear
recognized_faces = recognition(imagenes_a_rastrear)

# Imprimir las ubicaciones de las caras reconocidas
print("Ubicaciones de las caras reconocidas:", recognized_faces)

cv2.destroyAllWindows()  # Cerrar todas las ventanas de OpenCV al final


#########



import cv2
import face_recognition

def recognition(image_person):

    recognized_faces = []


    imagen_persona = face_recognition.load_image_file(image_person)
        
    face_locations = face_recognition.face_locations(imagen_persona)

    if len(face_locations) > 0:
        imagen_persona_encodings = face_recognition.face_encodings(imagen_persona, face_locations)[0]

    # Cargar la imagen objetivo
    imagen_objetivo = face_recognition.load_image_file('buscamos.jpg')
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
recognition('lautaro.jpg')
# recognition('Sofia.jpg')