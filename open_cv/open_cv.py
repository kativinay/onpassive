import cv2
import numpy as np 

"""
OpenCV is the huge open-source library used for computer vision, machine learning, and image processing.
Image processing, Detection, Drawing functions, video processing are some of main features of open cv.
Image Processing:
    we can do image resizing, bluring image, rotating, shifting, converting color, image translation etc

Detection:
    we can do linear detection, circular detection, detecting cornors of image, find circles and ellipses 
    in image etc.

Drawing functions:
    we can draw a line, arrow segment, ellipses, circle, rectangle, text string etc.

video processing:
    we can converting multiple images into a video and extracting images from video.

"""
def converImagetoBW():
    """
    Iamge processing:
    reading image using open-cv
    """
    img = cv2.imread("open_cv\image.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cornerDetection():
    """
    Detecting the corners nodes of image.
    """
    image = cv2.imread('open_cv\image.jpg') 
    operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    operatedImage = np.float32(operatedImage) 
    dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07) 
    dest = cv2.dilate(dest, None) 
    image[dest > 0.01 * dest.max()]=[0, 0, 255] 
    cv2.imshow('Image with Borders', image) 
    if cv2.waitKey(0) & 0xff == 27: 
        cv2.destroyAllWindows() 

def drawCircle():
    """
    Drawing circle on image
    """
    image = cv2.imread('open_cv\image.jpg')
    center_coordinates = (120, 50)
    radius = 20
    color = (255, 0, 0) 
    thickness = 2
    image = cv2.circle(image, center_coordinates, radius, color, thickness)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# converImagetoBW()
# cornerDetection()
drawCircle()