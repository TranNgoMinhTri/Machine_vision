import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

class Image_processing(object):
    def __init__(self, image, threshold, inv = False):
        self.img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.img_threshold_binary  = cv2.threshold(self.img_gray, threshold, 255, cv2.THRESH_BINARY)[1]
        self.inv = inv
        if self.inv == True:
            self.img_threshold_inv = cv2.threshold(self.img_gray, threshold, 255, cv2.THRESH_BINARY_INV)[1]
        

    def _dilate(self, kernel, iter):
        if self.inv == True:
            img = cv2.dilate(self.img_threshold_inv, kernel = kernel, iterations=iter)
        else:
            img = cv2.dilate(self.img_threshold_binary, kernel = kernel, iterations=iter)
        print("Dilated with kernel =  {} and iteration = {}".format(kernel, iter))
        return img

    def _erode(self, kernel, iter):
        if self.inv == True:
            img = cv2.erode(self.img_threshold_inv, kernel = kernel, iterations=iter)
        else:
            img = cv2.erode(self.img_threshold_binary, kernel = kernel, iterations=iter)
        print("Eroded with kernel =  {} and iteration = {}".format(kernel, iter))
        return img
    def _histogram(self):
        plt.hist(self.img_gray.ravel(),256,[0,256])
        plt.show()
