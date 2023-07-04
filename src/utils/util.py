from .openCV import OpenCV

class Util:

    def loadImagePath(path):
        try:
            image = OpenCV.imageReader(path)
            rgbImage = OpenCV.cvtColor(image)
        
            return rgbImage
        except:
            raise TypeError('Error to load image path in Util') 
        
