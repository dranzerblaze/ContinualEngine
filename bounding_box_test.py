import os
import cv2

img = cv2.imread("1.png")
cv2.rectangle(img , ((int(9.3184692e+01) , int(3.6518726e+02)) , (int(7.1891809e+02) , int(7.6505688e+02)) , (255,255,0) ,2)
cv2.imshow("final" , img)
cv2.waitKey(0)