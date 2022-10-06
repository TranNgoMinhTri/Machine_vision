from traceback import print_tb
from cv2 import DIST_L2, mean
import numpy as np 
import cv2 
import matplotlib.pyplot as plt


img  =  cv2.imread("10.PNG", cv2.IMREAD_COLOR)
img_1 = cv2.imread("10.PNG", cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
# img_1 = cv2.resize(img_1,(int(img_1.shape[1]/2), int(img_1.shape[0]/2)))

def his(image):
    b,g,r = cv2.split(img)
    fig = plt.figure(figsize=(8,4))

    ax = fig.add_subplot(121)
    ax.imshow(img[...,::-1])

    ax = fig.add_subplot(122)
    for x, c in zip([b,g,r], ["b", "g", "r"]):
        xs = np.arange(256)
        ys = cv2.calcHist([x], [0], None, [256], [0,256])
        ax.plot(xs, ys.ravel(), color=c)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()
def morph(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))    
    img = cv2.morphologyEx(image,cv2.MORPH_CLOSE , kernel, iterations = 1)
    # img = cv2.dilate(img,kernel,iterations=1)
    return img
def __removeSmallContours(mask):
    image_binary = np.ones((mask.shape[0], mask.shape[1]), np.uint8)
    contours = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 350.0:
            print(area)
            masked = cv2.drawContours(image_binary, cnt, -1, (255,255,255), 1)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))   
    masked = cv2.dilate(masked,kernel,iterations=2)
    return masked




g_img = cv2.GaussianBlur(img_1,(7,7),0)
b_img = cv2.threshold(g_img, 120,255,cv2.THRESH_BINARY_INV)[1]
b_img_m = morph(b_img)
# b_img_rm = __removeSmallContours(b_img_m)

dist_img = cv2.distanceTransform(b_img_m,cv2.DIST_L2,3)
cv2.normalize(dist_img, dist_img, 0,1,cv2.NORM_MINMAX)
out = cv2.threshold(dist_img, 0.48,255,cv2.THRESH_BINARY)[1] 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))   

out = cv2.erode(out,kernel,iterations = 3 )   
out = np.array(out, dtype=np.uint8)

contours = cv2.findContours(out, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
# wt = cv2.watershed(img_1, out)

hist = cv2.calcHist([img_1],[0],None,[256],[0,256])
cv2.imshow("gray", img_1)
cv2.imshow("binary_1", b_img)
# cv2.imshow("binary_2", b_img_m)
# cv2.imshow("rm_cnt", b_img_rm)
# cv2.imshow("dist", dist_img)
# cv2.imshow("out", out )
# cv2.imshow("color", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# print(len(contours))
