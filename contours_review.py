import cv2
import numpy as np
from image_processing import Image_processing
img = cv2.imread("small_holes.jpg", cv2.IMREAD_COLOR)

img_p = Image_processing(img, 150, inv=True)

img_gray = img_p.img_gray
b_img = img_p.img_threshold_inv

cnt, hierachy = cv2.findContours(b_img,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for i,cnt in enumerate(cnt):
    if cv2.contourArea(cnt) > 100:
        centers[i], radius[i] = cv2.minEnclosingCircle(cnt[i])
        cv2.circle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #cv.putText(img, str(i+1),(x,y),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
cv2.imshow("color", img)
cv2.imshow("image", b_img)
print(hierachy)
cv2.waitKey(0)
cv2. destroyAllWindows()
