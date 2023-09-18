import cv2
import threading
import numpy as np

shared_cube = None
shared_pillar = None

sync_event = threading.Event()

def process_frames():
	global shared_cube
	global shared_pillar
	cube = None
	pillar = None
	cap = cv2.VideoCapture(0)
	while True:
		with shared_variables_lock:
			shared_cube = None
			shared_pillar = None
		ret, frame = cap.read()
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		#color range(HSV)
		low_red = np.array([-17, 169,   58])
		high_red = np.array([ 24, 280, 277])
		low_green = np.array([ 47, 131, 46])
		high_green = np.array([ 87, 251, 156])
		low_blue = np.array([ 86, 167,  66])
		high_blue = np.array([125, 287, 186])
		low_yellow = np.array([  25, 188,  104])
		high_yellow = np.array([ 47, 255, 224])

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
			x,y,w,h = cv2.boundingRect(contour)
			red_xywh = [x,y,w,h,color]
			colorlist.append(red_xywh)
				
		contours, hieracrchy = cv2.findContours(morph_green,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Green'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			x,y,w,h = cv2.boundingRect(contour)
			green_xywh = [x,y,w,h,color]
			colorlist.append(green_xywh)

		contours, hieracrchy = cv2.findContours(morph_blue,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Blue'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			x,y,w,h = cv2.boundingRect(contour)
			blue_xywh = [x,y,w,h,color]
			colorlist.append(blue_xywh)

		contours, hieracrchy = cv2.findContours(morph_yellow,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		color = 'Yellow'
		if len(contours) != 0:
			contour = max(contours, key = cv2.contourArea)
			x,y,w,h = cv2.boundingRect(contour)
			yellow_xywh = [x,y,w,h,color]
			colorlist.append(yellow_xywh)

		if len(colorlist) == 0:
			pass			
		elif len(colorlist) == 1:
			pillar = colorlist[0][4]
		elif len(colorlist) == 2:
			if colorlist[0][3] > colorlist[1][3]:
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
			print(colorlist)
			if colorlist[0][3] > colorlist[1][3]:
				pillar = colorlist[0][4]
				cube = colorlist[1][4]
			else:
				cube = colorlist[0][4]
				pillar = colorlist[1][4]
		print(pillar)
		with shared_variables_lock:
			shared_cube = cube
			shared_pillar = pillar
		sync_event.set()
		sync_event.clear()

def print_everything():
	global shared_cube
	global shared_pillar
	while True:
		sync_event.wait()
		with shared_variables_lock:
			cube = shared_cube
			pillar = shared_pillar
		print(pillar)
		print(cube)

shared_variables_lock = threading.Lock()
processing_thread = threading.Thread(target = process_frames)
print_thread = threading.Thread(target = print_everything)

processing_thread.start()
print_thread.start()

processing_thread.join()
print_thread.join()
