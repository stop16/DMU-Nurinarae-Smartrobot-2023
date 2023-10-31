#Whole new color detecting

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

VM_Pillar = [
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]

VM_Cube = [
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]

def whole_new_color_detection(loc,dir):
    frame_cnt = 0
    while True:
        ret, frame = cap.read()
        if frame_cnt == 50:
            break
        if ret:
            frame_cnt+=1
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    filename = str(loc) + '-' + str(dir) + '.jpg'
    cv2.imwrite(filename, frame)

    #color range(HSV)
    low_red = np.array([157,  144, 71])
    high_red = np.array([197,  255, 255])
    low_green = np.array([56, 189, 31])
    high_green = np.array([96, 255, 255])
    low_blue = np.array([88, 160, 81])
    high_blue = np.array([128, 255, 255])
    low_yellow = np.array([4, 136, 103])
    high_yellow = np.array([44, 255, 255])

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

    print(len(colorlist))
    print(colorlist)
    
    if len(colorlist) == 1:
        VM_Pillar[loc][dir] = colorlist[0][4]
    elif len(colorlist) == 2:
        if colorlist[0][3] > colorlist[1][3]:
            VM_Pillar[loc][dir] = colorlist[0][4]
            VM_Cube[loc][dir] = colorlist[1][4]
        else:
            VM_Cube[loc][dir] = colorlist[0][4]
            VM_Pillar[loc][dir] = colorlist[1][4]
    elif len(colorlist) == 3:
        for i in range(len(colorlist)):
            if colorlist[i][4] == 'Yellow':
                break
        colorlist.pop(i)
        print(colorlist)
        if colorlist[0][3] > colorlist[1][3]:
            VM_Pillar[loc][dir] = colorlist[0][4]
            VM_Cube[loc][dir] = colorlist[1][4]
        else:
            VM_Cube[loc][dir] = colorlist[0][4]
            VM_Pillar[loc][dir] = colorlist[1][4]
whole_new_color_detection(0,0)
print(VM_Cube) 
print(VM_Pillar)