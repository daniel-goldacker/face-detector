# face-detector

This Python program loads a reference photo, detects the face in the photo, and extracts the facial features. Then he launches the camera and extracts the facial features and compares them with the features in the reference photo saying whether or not he knows the person. In this example, we use the face_recognition library to perform face recognition, which is a face recognition library.

NOTE: This program does not have the ability to distinguish whether what is in front of the camera is really a person. We will do this implementation in a second moment.

To run it, follow the steps below:

1. Place in directory **./src**:
```sh
cd src
```
2. Install additional libraries:
```sh
pip install -r requirements.txt
```
3. add a photo of the face in the ./src/image directory with the name 'photo_reference.jpg'.

4. Run the integration:
```sh
run manager.py
```