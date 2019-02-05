import cv2
import numpy as np

img = cv2.imread('C:\\Users\\58050379\\PycharmProjects\\Floc Detection in Water Treatment Process\\2\\Flocs-3-700x593.jpg')

kernel = np.ones((7,7),np.uint8)
roi = img[: , :]
rows, cols, _ = roi.shape
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#gray_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)

gray_roi = cv2.erode(gray_roi,kernel,iterations = 1)
#gray_roi = cv2.morphologyEx(gray_roi, cv2.MORPH_OPEN, kernel)

#_, threshold = cv2.threshold(gray_roi, 127, 255, cv2.THRESH_BINARY_INV)
_, threshold = cv2.threshold(gray_roi,255,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#_, threshold = cv2.adaptiveThreshold(gray_roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

count = 0
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    area = w*h
    if area < 4000:
        count = count+1
        cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 1)
        #cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.rectangle(roi, (0, 0), (200, 30), (255,255,255), -1)
cv2.putText(roi,'Number of Floc : ' + str(count),
        (10,20),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font
        0.5,                      # fontScale
        (0,0,0),                  # fontColor
        1)                        # lineType

cv2.imshow("Threshold", threshold)
#cv2.imshow("gray roi", gray_roi)
cv2.imshow("Roi", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()

def draw_text_on_image(img_draw, count_yellow, count_orange):
    cv2.rectangle(img_draw, (0, 0), (500, 120), (0,0,0), -1)
    cv2.putText(img_draw,'Orange Count : ' + str(count_orange),
        (10,50),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font
        1.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    cv2.putText(img_draw,'Yellow Count : ' + str(count_yellow),
        (10,100),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font
        1.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    return img_draw
