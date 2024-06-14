import ctypes
import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

    def load_encoding_images(self, images_path):
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.jpg"))

        print(f"{len(images_path)} encoding images found.")

        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename without the extension
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            # Encode the loaded images into a feature vector
            img_encodings = face_recognition.face_encodings(rgb_img)
            if img_encodings:
                img_encoding = img_encodings[0]
                self.known_face_encodings.append(img_encoding)
                self.known_face_names.append(filename)
            else:
                print(f"No faces found in image: {img_path}")

    def detect_known_faces(self, frame):
        # Detect all faces in the frame
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Find distances to the known faces
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Convert face locations back to original size
        face_locations = [(top*4, right*4, bottom*4, left*4) for top, right, bottom, left in face_locations]

        return face_locations, face_names
