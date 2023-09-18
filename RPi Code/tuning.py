#tuning_new!

import cv2 
import numpy as np 
from PWM_Test import *

webcam = cv2.VideoCapture(0)
"""
	참고 사이트(Color Picker)
	https://colorpicker.me/#050505

	HSV에 대한 설명
	H : 색상, 0~360의 범위를 가지지만 OpenCV에서는 1/2만큼 줄여 0~180의 범위를 가집니다.
	S : 채도, 값이 0에 가까우면 하얀색, 255에 가까울수록 H의 색이 됩니다.
	V : 명도, 값이 0에 가까우면 검은색, 255에 가까울수록 H의 색이 됩니다.
"""
def get_val_from_image(event, x, y, flags, image):
    hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    value = np.array(hsv_image[y,x])
    if event == cv2.EVENT_LBUTTONDOWN:
        h = int(value[0])
        s = int(value[1])
        v = int(value[2])
        print("마우스 왼쪽 버튼이 눌린 위치의 HSV값은 : "+str(h)+","+str(s)+","+str(v))

    if event == cv2.EVENT_LBUTTONUP:
        lower_mask = np.array([value[0]-20, value[1]-40, value[2]-80])
        upper_mask = np.array([value[0]+20, value[1]+40, value[2]+80])
        mask = cv2.inRange(hsv_image,lower_mask, upper_mask)
        range_image = cv2.bitwise_and(image, image, mask=mask)
        print("현재 위치에서 색의 범위는 : ",lower_mask, upper_mask)
        cv2.imshow('result',range_image)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('a'):
        cam_to_left()
    if key == ord('s'):
        cam_to_center()
    if key == ord('d'):
        cam_to_right()
    if key == ord('q'):
        break
    _, origin_image = webcam.read()
    imageinput = origin_image
    small_img = cv2.resize(imageinput,(960,540))
    cv2.imshow('image', small_img)
    cv2.setMouseCallback('image', get_val_from_image, small_img)
