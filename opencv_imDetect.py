import cv2 as cv
import numpy as numpy
import matplotlib.pyplot as pyplot

# Load image into grayscale. Aso can read as
# IMREAD_COLOR, IMREAD_UNCHAGNED
img = cv.imread('watch.jpg', cv.IMREAD_GRAYSCALE)