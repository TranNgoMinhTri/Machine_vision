from msvcrt import kbhit
from tkinter import image_names
import cv2 as cv 
import numpy as np
import time
cTime1 = time.time()
def change_pixel(img, img_final):
    for i in range(3):
        img_final[x,y,i] = img[x,y,i]

img = cv.imread("halloween.jpg", cv.IMREAD_COLOR)
mask = cv.imread("mask.jpg", cv.IMREAD_GRAYSCALE)
w = img.shape[0]
h = img.shape[1]

img_resh = np.reshape(mask, (1,w*h))
a = np.argwhere(img_resh[0] <10)

img_final = np.copy(img) 
img_final[:,:,:] = [255,255,255]

for i in a[:]:
    x = int(i/626)
    y = int(i%626)
    change_pixel(img, img_final)

cTime2 = time.time()
print(cTime2- cTime1)

cv.imshow("image", img_final) 
cv.imshow("mask", mask)

cv.waitKey(0)
cv.destroyAllWindows()
