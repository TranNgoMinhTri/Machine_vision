import cv2
from image_processing import Image_processing

img = cv2.imread("10.PNG", cv2.IMREAD_COLOR)

img = Image_processing(img, 150)

b_img = img._dilate(kernel=(7,7),iter=10)

cv2.imshow("image_b",b_img)
# cv2.imshow("image_inv",img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()