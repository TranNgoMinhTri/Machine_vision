from msvcrt import kbhit
from tkinter import image_names
import cv2 as cv 
import numpy as np
import time
cTime1 = time.time()
img = cv.imread("halloween.jpg", cv.IMREAD_COLOR)
mask = cv.imread("mask.jpg", cv.IMREAD_GRAYSCALE)
w = img.shape[0]
h = img.shape[1]
cv.findContours(mask, cv.RETR_EXTERNAL, )

cTime2 = time.time()
print(cTime2- cTime1)

cv.imshow("image", ) 
cv.imshow("mask", mask)

cv.waitKey(0)
cv.destroyAllWindows()
