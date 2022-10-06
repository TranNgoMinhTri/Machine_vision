import cv2
import numpy as np
from image_processing import Image_processing

def drawcontours(contours, image):
    for i,cnt in enumerate(contours):
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image,(x,y),(x+w,y+h),(np.random.randint(1,255),np.random.randint(1,255),np.random.randint(1,255)),2)
        cv2.putText(img, str(i+1),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)



img = cv2.imread("small_holes.jpg", cv2.IMREAD_COLOR)
img_p = Image_processing(img, 150, inv=True)
img_gray = img_p.img_gray
b_img = img_p.img_threshold_inv
cnt, hierachy = cv2.findContours(b_img,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


drawcontours(cnt, img)
img_p._histogram()
cv2.imshow("image_b",img)
# cv2.imshow("image_inv",img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()