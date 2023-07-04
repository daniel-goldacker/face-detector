import face_recognition

class FaceDetector:

    def compareFaces(encodingsReference, encodingCamera):
        try:
            return face_recognition.compare_faces(encodingsReference, encodingCamera)
        except:
            raise TypeError('Error to commpare faces in FaceDetector') 
        

    def faceEncoding(faceImage, knownFaceLocations=None, numJitters=1, Model="small"):
        try:
            return face_recognition.face_encodings(faceImage, knownFaceLocations, numJitters, Model)
        except:
            raise TypeError('Error to face encoding in FaceDetector') 


    def faceLocations(frame):
        try:
            return face_recognition.face_locations(frame)
        except:
            raise TypeError('Error to face locations in FaceDetector') 
    
