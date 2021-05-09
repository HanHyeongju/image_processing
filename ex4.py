import cv2
import numpy as np

img = cv2.imread('morph_dot.png')

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))

dilation_rect = cv2.dilate(img, kernel_rect)

merged1 = np.hstack((img, dilation_rect))
cv2.imshow('Dilation_rect', merged1)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilation_ellipse = cv2.dilate(img, kernel_ellipse)

merged2 = np.hstack((img, dilation_ellipse))
cv2.imshow('Dilation_ellipse', merged2)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilation_cross = cv2.dilate(img, kernel_cross)

merged3 = np.hstack((img, dilation_cross))
cv2.imshow('Dilation_cross', merged3)
cv2.waitKey(0)
cv2.destroyAllWindows()