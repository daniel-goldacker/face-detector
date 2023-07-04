import cv2

class OpenCV:

    RED = (0, 0, 255)
    GREEN = (0, 255, 0)


    def cvtColor(image):
        try:
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except:
            raise TypeError('Error to cvtColor in OpenCV') 
        

    def destroyAllWindows():
        try:
            cv2.destroyAllWindows()
        except:
            raise TypeError('Error to destroy all windows in OpenCV')     

    
    def exit(key):
        try:
            if cv2.waitKey(1) & 0xFF == ord(key):
                return True
            else:
                return False
        except:
            raise TypeError('Error to key detection for exit in OpenCV') 
    

    def imshow(text, frame):
        try:
            cv2.imshow(text, frame)
        except:
            raise TypeError('Error to imshow in OpenCV') 
    

    def imageReader(path):
        try:
            return cv2.imread(path)
        except:
            raise TypeError('Error to image reader in OpenCV') 
    

    def putText(frame, text, color):
        try:
            cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        except:
            raise TypeError('Error to put text in OpenCV') 
        

    def videoCapture():
        try:
            return cv2.VideoCapture(0)
        except:
            raise TypeError('Error to video capture in OpenCV') 

