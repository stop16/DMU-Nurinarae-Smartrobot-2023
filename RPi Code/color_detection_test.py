import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def get_picture():
    time.sleep(2)
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return hsv_frame

def color_detection_and_contours(img):
    #색 범위 설정(HSV)
    low_red = np.array([157,  144, 101])
    high_red = np.array([197,  255, 255])
    low_green = np.array([56, 189, 61])
    high_green = np.array([96, 255, 255])
    low_blue = np.array([88, 160, 111])
    high_blue = np.array([128, 255, 255])
    low_yellow = np.array([4, 136, 133])
    high_yellow = np.array([44, 255, 255])

    #mask creation
    red_mask = cv2.inRange(img, low_red, high_red)
    green_mask = cv2.inRange(img, low_green, high_green)
    blue_mask = cv2.inRange(img, low_blue, high_blue)
    yellow_mask = cv2.inRange(img, low_yellow, high_yellow)

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
    red_xywh = []
    green_xywh = []
    blue_xywh = []
    yellow_xywh = []
    countours, hieracrchy = cv2.findContours(morph_red,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    color = 'red'
    for pic, contour in enumerate(countours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x,y,w,h = cv2.boundingRect(contour)
            red_xywh = x,y,w,h,color
    countours, hieracrchy = cv2.findContours(morph_green,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    color = 'green'
    for pic, contour in enumerate(countours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x,y,w,h = cv2.boundingRect(contour)
            green_xywh = x,y,w,h,color
    countours, hieracrchy = cv2.findContours(morph_blue,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    color = 'blue'
    for pic, contour in enumerate(countours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x,y,w,h = cv2.boundingRect(contour)
            blue_xywh = x,y,w,h,color
    countours, hieracrchy = cv2.findContours(morph_yellow,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    color = 'yellow'
    for pic, contour in enumerate(countours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x,y,w,h = cv2.boundingRect(contour)
            yellow_xywh = x,y,w,h,color
    
    return red_xywh, green_xywh, blue_xywh, yellow_xywh

def get_num_of_value(val):
    cnt = 0
    for i in range(len(val)):
        if val[i]:
            cnt+=1

#기둥, 큐브 순으로 반환
def decision(val):
    first_object = []
    second_object = []
    if get_num_of_value(val) == 0:
        pass
    elif get_num_of_value(val) == 1:
        for i in range(len(val)):
            break
        return val[i][4]
    elif get_num_of_value(val) == 2:
        for i in range(len(val)):
            val[i] = first_object
        for i in range(i+1,len(val)):
            val[i] = second_object
        if first_object[3] > second_object[3]:
            return first_object,second_object
        elif first_object[3] < second_object[3]:
            return second_object,first_object
