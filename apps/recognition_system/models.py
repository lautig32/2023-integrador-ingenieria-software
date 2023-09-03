import cv2
import tempfile
import face_recognition

from django.core.files.base import ContentFile

class FaceRecognition:
    def __init__(self, image_list):
        self.image_list = image_list
        self.encodings_personas_interes = []
        self.load_person_images()

    def load_person_images(self):
        self.encodings_personas_interes = []
        
        for image_file in self.image_list:
            image_file = image_file.lstrip('/')
            imagen_persona = face_recognition.load_image_file(image_file)
            
            # Obtiene las codificaciones de rostros para esta imagen de persona
            codificaciones = face_recognition.face_encodings(imagen_persona)
            
            # Agrega cada codificación por separado a la lista
            for codificacion in codificaciones:
                self.encodings_personas_interes.append(codificacion)


    def recognize_faces(self, imagen_objetivo_path):
        recognized_faces = []

        imagen_objetivo_path = imagen_objetivo_path.lstrip('/')

        imagenes_objetivo = [
            face_recognition.load_image_file(imagen_objetivo_path),
        ]

        for imagen_objetivo in imagenes_objetivo:
            imagen_objetivo_copy = imagen_objetivo.copy()
            
            rostros_objetivo = face_recognition.face_locations(imagen_objetivo)
            
            for rostro_objetivo in rostros_objetivo:
                imagen_objetivo_encodings = face_recognition.face_encodings(imagen_objetivo, [rostro_objetivo])[0]
                face_recognized = False

                for encoding_persona_interes in self.encodings_personas_interes:
                    resultado = face_recognition.compare_faces([encoding_persona_interes], imagen_objetivo_encodings)[0]
                    if resultado:
                        recognized_faces.append(rostro_objetivo)
                        top, right, bottom, left = rostro_objetivo
                        cv2.rectangle(imagen_objetivo_copy, (left, top), (right, bottom), (0, 255, 0), 2)
                        face_recognized = True

                if not face_recognized:
                    top, right, bottom, left = rostro_objetivo
                    cv2.rectangle(imagen_objetivo_copy, (left, top), (right, bottom), (0, 0, 255), 2)

            temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
            temp_filename = temp_file.name
            cv2.imwrite(temp_filename, imagen_objetivo_copy)

            with open(temp_filename, 'rb') as temp_file:
                temp_data = temp_file.read()

            # Crear un ContentFile a partir de los datos del archivo temporal
            temp_content_file = ContentFile(temp_data)

            return temp_content_file