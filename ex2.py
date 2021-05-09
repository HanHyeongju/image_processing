import cv2
title_window = 'Canny edge'
#threshold 첫 값 지정
th_high = 200
th_low = 100

#canny edge
road = cv2.imread('road.png', cv2.IMREAD_GRAYSCALE)
canny_edge = cv2.Canny(road, 100, 200)

#스크롤 조절창 박기
cv2.namedWindow(title_window)

#trackbar 생성
#hign보다 큰 값을 확실히 edge, 작은 값은 확실히 edge아님
def on_trackbar_high(val):
    global th_high
    global th_low
    th_high = val
    canny_edge = cv2.Canny(road, th_low, th_high)
    cv2.imshow(title_window, canny_edge)

def on_trackbar_low(val):
    global th_low
    global th_high
    th_low = val
    canny_edge = cv2.Canny(road, th_low, th_high)
    cv2.imshow(title_window, canny_edge)

#트랙바 만들기
cv2.createTrackbar("High", title_window, th_high, 300, on_trackbar_high)
cv2.createTrackbar("Low", title_window, th_low, 300, on_trackbar_low)

cv2.imshow(title_window, canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()