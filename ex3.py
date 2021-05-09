import cv2
import numpy as np

#canny edge
road = cv2.imread('road.png', cv2.IMREAD_COLOR)
road_gray = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
canny_edge = cv2.Canny(road_gray, 100, 200)

#canny edge 결과물에 roi 적용 : 도로만 따기
road_mask = cv2.imread('road_mask.png', cv2.IMREAD_GRAYSCALE)
roi = cv2.bitwise_and(canny_edge, road_mask)

#hough transform - line따기
#cv2.HoughLines(image, rho, theta, threshold, ..)
lines = cv2.HoughLines(roi, 1, np.pi/180, 80)

for i in range(len(rho, theta)):
    for rho, theta in lines [i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(road, (x1, y1), (x2, y2), (0,0,255), 2)

    cv2.imshow('road', road)

    cv2.waitKey(0)
    cv2.destroyAllWindows()