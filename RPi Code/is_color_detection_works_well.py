import cv2
import numpy as np
import time

def process_frames():
	global shared_cube
	global shared_pillar
	cap = cv2.VideoCapture(-1)
	cube = 0
	pillar = 0
	while True:
		try:
			ret, frame = cap.read()
		except:
			while not ret:
				ret, frame = cap.read()
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		#color range(HSV)
		low_red = np.array([156, 121,   77])
		high_red = np.array([ 196, 241, 319])
		low_green = np.array([ 56, 103, 58])
		high_green = np.array([ 96, 223, 218])
		low_blue = np.array([ 87, 167,  129])
		high_blue = np.array([127, 260, 329])
		low_yellow = np.array([  8, 128,  128])
		high_yellow = np.array([ 43, 248, 335])

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

		#create contours
		colorlist = []
		contours, hieracrchy = cv2.findContours(morph_red,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Red'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			if cv2.contourArea(contour) > 300:
				x,y,w,h = cv2.boundingRect(contour)
				red_xywh = [x,y,w,h,color]
				colorlist.append(red_xywh)
				
		contours, hieracrchy = cv2.findContours(morph_green,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Green'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			if cv2.contourArea(contour) > 300:
				x,y,w,h = cv2.boundingRect(contour)
				green_xywh = [x,y,w,h,color]
				colorlist.append(green_xywh)

		contours, hieracrchy = cv2.findContours(morph_blue,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Blue'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			if cv2.contourArea(contour) > 300:
				x,y,w,h = cv2.boundingRect(contour)
				blue_xywh = [x,y,w,h,color]
				colorlist.append(blue_xywh)

		contours, hieracrchy = cv2.findContours(morph_yellow,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Yellow'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			if cv2.contourArea(contour) > 300:
				x,y,w,h = cv2.boundingRect(contour)
				yellow_xywh = [x,y,w,h,color]
				colorlist.append(yellow_xywh)

		if len(colorlist) == 0:
			cube = 'None'
			pillar = 'None'
		elif len(colorlist) == 1:
			cube = 'None'
			pillar = colorlist[0][4]
		elif len(colorlist) == 2:
			if colorlist[0][4] == 'Yellow' or colorlist[1][4] == 'Yellow':
				pillar = 'Yellow'
				cube = 'None'
			else:
				if colorlist[0][1] > colorlist[1][1]:
					pillar = colorlist[0][4]
					cube = colorlist[1][4]
				else:
					cube = colorlist[0][4]
					pillar = colorlist[1][4]
		elif len(colorlist) == 3:
			for i in range(len(colorlist)):
				if colorlist[i][4] == 'Yellow':
					break
			colorlist.pop(i)
			if colorlist[0][1] > colorlist[1][1]:
				pillar = colorlist[0][4]
				cube = colorlist[1][4]
			else:
				cube = colorlist[0][4]
				pillar = colorlist[1][4]
		print("pillar : " + str(pillar))
		print("cube : " + str(cube))
		time.sleep(0.1)
process_frames()
