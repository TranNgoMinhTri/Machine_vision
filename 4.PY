from traceback import print_tb
from cv2 import DIST_L2, mean
import numpy as np 
import cv2 

img  =  cv2.imread("coin.png", cv2.IMREAD_COLOR)
img_1 = cv2.imread("coin.png", cv2.IMREAD_GRAYSCALE)
b_img = cv2.threshold(img_1, 150,255,cv2.THRESH_BINARY_INV)[1]

dist_img = cv2.distanceTransform(b_img,cv2.DIST_L2,3)
cv2.normalize(dist_img, dist_img, 0,1,cv2.NORM_MINMAX)
out = cv2.threshold(dist_img, 0.55,255,cv2.THRESH_BINARY)[1]    
out = np.array(out, dtype=np.uint8)

contours = cv2.findContours(out, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
for i, cnt in enumerate(contours):
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0))

cv2.imshow("binary", b_img)
cv2.imshow("dist", dist_img)
cv2.imshow("out", out)
cv2.imshow("color", img)

cv2.waitKey(0)
cv2.destroyAllWindows()