import cv2

road = cv2.imread('road.png', cv2.IMREAD_GRAYSCALE)
canny_edge = cv2.Canny(road, 100, 200)

cv2.imshow('Canny', canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()