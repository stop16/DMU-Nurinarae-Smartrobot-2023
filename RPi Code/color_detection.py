import cv2
import numpy as np
from PWM_Test import *

cap = cv2.VideoCapture(-1)

while True:
	_, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	"""
	참고 사이트(Color Picker)
	https://colorpicker.me/#050505

	HSV에 대한 설명
	H : 색상, 0~360의 범위를 가지지만 OpenCV에서는 1/2만큼 줄여 0~180의 범위를 가집니다.
	S : 채도, 값이 0에 가까우면 하얀색, 255에 가까울수록 H의 색이 됩니다.
	V : 명도, 값이 0에 가까우면 검은색, 255에 가까울수록 H의 색이 됩니다.
	"""

	#color range(HSV)
	low_red = np.array([155, 101,   67])
	high_red = np.array([ 196, 241, 319])
	low_green = np.array([ 47, 127, 54])
	high_green = np.array([ 87, 255, 206])
	low_blue = np.array([ 87, 195,  36])
	high_blue = np.array([127, 279, 218])
	low_yellow = np.array([  5, 108,  125])
	high_yellow = np.array([ 45, 213, 285])


	#mask creation
	red_mask = cv2.inRange(hsv_frame, low_red, high_red)
	green_mask = cv2.inRange(hsv_frame, low_green, high_green)
	blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
	yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)

	#apply mask
	kernel_3 = np.ones((3,3),np.uint8)
	kernel_5 = np.ones((5,5),np.uint8)
	morph_red = cv2.morphologyEx(red_mask,cv2.MORPH_OPEN,kernel_3)
	morph_red = cv2.morphologyEx(red_mask,cv2.MORPH_DILATE,kernel_5)
	morph_green = cv2.morphologyEx(green_mask,cv2.MORPH_OPEN,kernel_3)
	morph_green = cv2.morphologyEx(green_mask,cv2.MORPH_DILATE,kernel_5)
	morph_blue = cv2.morphologyEx(blue_mask,cv2.MORPH_OPEN,kernel_3)
	morph_blue = cv2.morphologyEx(blue_mask,cv2.MORPH_DILATE,kernel_5)
	morph_yellow = cv2.morphologyEx(yellow_mask,cv2.MORPH_OPEN,kernel_3)
	morph_yellow = cv2.morphologyEx(yellow_mask,cv2.MORPH_DILATE,kernel_5)
	
	# RGB Color Bitwising
	red = cv2.bitwise_and(frame, frame, mask=morph_red)
	blue = cv2.bitwise_and(frame, frame, mask=morph_blue)
	green = cv2.bitwise_and(frame, frame, mask=morph_green)

	# Every color except white
	low = np.array([0, 42, 0])
	high = np.array([179, 255, 255])
	mask = cv2.inRange(hsv_frame, low, high)
	result = cv2.bitwise_and(frame, frame, mask=mask)

	"""
	# apply morphology
	kernel = np.ones((20,20), np.uint8)
	morph = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	kernel = np.ones((5,5), np.uint8)
	morph = cv2.morphologyEx(morph, cv2.MORPH_DILATE, kernel)
    """
    
	# Creating contour to track red color
	contours, hierarchy = cv2.findContours(morph_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv2.boundingRect(contour) 
			frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) 
			
			cv2.putText(frame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
	
	# Creating contour to track green color 
	contours, hierarchy = cv2.findContours(morph_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv2.boundingRect(contour) 
			frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
			
			cv2.putText(frame, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0)) 

	# Creating contour to track blue color 
	contours, hierarchy = cv2.findContours(morph_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv2.boundingRect(contour) 
			frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
			
			cv2.putText(frame, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

	# Creating contour to track green color 
	contours, hierarchy = cv2.findContours(morph_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv2.boundingRect(contour) 
			frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2) 
			
			cv2.putText(frame, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
	
	cv2.imshow("Frame", frame)
	#cv2.imshow("Red", red)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    #cv2.imshow("Result", result)

	key = cv2.waitKey(1) & 0xFF
	if key == ord('a'):
		cam_to_left()
	if key == ord('s'):
		cam_to_center()
	if key == ord('d'):
		cam_to_right()
	if key == ord('q'):
		break
