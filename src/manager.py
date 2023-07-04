from config import Config, ConfigFiles
from utils.faceDetector import FaceDetector
from utils.openCV import OpenCV
from utils.util import Util

try:
    # Load the reference photo
    photoReference = Util.loadImagePath(ConfigFiles.PHOTO_REFERENCE)

    # Extract face features from reference photo
    encodingsReference = FaceDetector.faceEncoding(photoReference)

    # Initialize the camera
    cap = OpenCV.videoCapture()

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Find the faces in the camera image
        facesCamera = FaceDetector.faceLocations(frame)

        if len(facesCamera) > 0:
            # Extract face features from camera
            encodingsCamera = FaceDetector.faceEncoding(frame, facesCamera)

            # Compare the encodings of the reference photo with those of the camera
            for encodingCamera in encodingsCamera:
                resultados = FaceDetector.compareFaces(encodingsReference, encodingCamera)
                if True in resultados:
                    OpenCV.putText(frame, "Recognized person", OpenCV.GREEN)
                else:
                    OpenCV.putText(frame, "Unknown person", OpenCV.RED)
        else:
            OpenCV.putText(frame, "No person on camera", OpenCV.RED)

        OpenCV.imshow("Person Verification (Press '" + Config.EXIT_KEY + "' for exit )", frame)

        if OpenCV.exit(Config.EXIT_KEY):
            break

except Exception as error:
    print(error)

finally:
    cap.release()
    OpenCV.destroyAllWindows()
