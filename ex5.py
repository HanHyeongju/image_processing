import cv2
import numpy as np

img = cv2.imread('morph_dot.png')
dilation_rect = cv2.imread('dilation_rect.png')

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

dilation_rect_2x = cv2.dilate(img, kernel_rect, iterations=2)

merged1 = np.hstack((img, dilation_rect, dilation_rect_2x))
cv2.imshow('final', merged1)
cv2.waitKey(0)
cv2.destroyAllWindows()
