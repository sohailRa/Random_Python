import cv2 as cv
import numpy as numpy
import matplotlib.pyplot as plt

#------------------------------ LOAD/WRITE IMAGES------------------------------------

# # Load image into grayscale. Aso can read as
# # IMREAD_COLOR, IMREAD_UNCHAGNED, IMREAD_GRAYSCALE
# img = cv.imread('/home/sohail/Documents/Random_Python/watch.jpg', cv.IMREAD_COLOR)

# # Show image using OpenCV
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # Show image using matplotlib
# # plt.imshow(img, cmap='gray', interpolation='bicubic')
# # plt.show()

# # Save image by
# cv.imwrite('watchgray.png', img)


#------------------------------ LOAD VIDEOS------------------------------------
# # Loading images from webcame (0) means # of webcame if more than 1 exists
# cap = cv.VideoCapture(0)
# # To save we used codec
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', forcc, 20.0, (640,480))

# while True:
# 	ret, frame = cap.read()
# 	out.write(frame)
# 	cv.imshow('frame', frame)

# 	if cv.waitKey(1) & 0xFF == ord('q'):
# 		break

# cap.release()
# out.release()
# cv.destroyAllWindows()


#------------------------------ DRAWING AND WRITING ON IMAGE------------------------------------
img = cv.imread('/home/sohail/Documents/Random_Python/watch.jpg', cv.IMREAD_COLOR)

# # Lets draw a line on image. OpenCV is BRG not RGB
# # if want blue we use (255,0,0), RED(0.255.0)
# # white color is (255,255,255)
# #line(which image, start point, end point, color of line, line width)
# cv.line(img, (0,0), (150, 150), (255, 255, 255), 15)

# Lets draw rectangle
#rectangle(image, start, end, color, width)
cv.rectangle(img, (50,20), (200,160), (0,255,0), 3)




cv.imshow('image', img)
cv.waitKey(0)	
cv.destroyAllWindows()