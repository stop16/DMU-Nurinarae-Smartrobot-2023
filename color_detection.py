import cv2
import numpy as np

cap = cv2.VideoCapture(0)

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

	# Red color(HSV Range)
	low_red = np.array([157,  144, 71])
	high_red = np.array([197,  255, 255])
	red_mask = cv2.inRange(hsv_frame, low_red, high_red)

	# apply morphology to Red
	kernel = np.ones((3,3), np.uint8)
	morph_red = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
	kernel = np.ones((5,5), np.uint8)
	morph_red = cv2.morphologyEx(morph_red, cv2.MORPH_DILATE, kernel)

    # Green color
	# Legacy Value
	#low_green = np.array([25, 52, 72])
	#high_green = np.array([102, 255, 255])
	low_green = np.array([56, 189, 31])
	high_green = np.array([96, 255, 255])
	green_mask = cv2.inRange(hsv_frame, low_green, high_green)

	# apply morphology to Green
	kernel = np.ones((3,3), np.uint8)
	morph_green = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
	kernel = np.ones((5,5), np.uint8)
	morph_green = cv2.morphologyEx(morph_green, cv2.MORPH_DILATE, kernel)

	# Blue color(HSV Range)
	# Legacy Value
	#low_blue = np.array([94, 80, 2])
	#high_blue = np.array([126, 255, 255])
	low_blue = np.array([88, 160, 81])
	high_blue = np.array([128, 255, 255])
	blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)

	# apply morphology to Blue
	kernel = np.ones((3,3), np.uint8)
	morph_blue = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
	kernel = np.ones((5,5), np.uint8)
	morph_blue = cv2.morphologyEx(morph_blue, cv2.MORPH_DILATE, kernel)

	# Yellow color
	low_yellow = np.array([4, 136, 103])
	high_yellow = np.array([44, 255, 255])
	yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)

	# apply morphology to Yellow
	kernel = np.ones((3,3), np.uint8)
	morph_yellow = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
	kernel = np.ones((5,5), np.uint8)
	morph_yellow = cv2.morphologyEx(morph_yellow, cv2.MORPH_DILATE, kernel)
	
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
	if key == ord('q'):
		break