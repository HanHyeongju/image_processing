import cv2
import numpy as np

road = cv2.imread('road.png', cv2.IMREAD_GRAYSCALE)
road_mask = cv2.imread('road_mask.png', cv2.IMREAD_GRAYSCALE)

dst = cv2.bitwise_and(road, road_mask)

cv2.imshow("ROI", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()