import pigpio
from time import sleep

pi = pigpio.pi()
pi.set_servo_pulsewidth(18,0)
pi.set_servo_pulsewidth(13,0)

def move_mg(num):
    if num == 0:
        pi.set_servo_pulsewidth(18,830)#MG996R to #1
        sleep(1)
    if num == 1:
        pi.set_servo_pulsewidth(18,1500)#MG996R to #2
        sleep(1)
    if num == 2:
        pi.set_servo_pulsewidth(18,2160)#MG996R to #3
        sleep(1)

def cam_to_center():
    pi.set_servo_pulsewidth(13,1500)#Camservo to Left
    sleep(1.5)

def cam_to_left():
    pi.set_servo_pulsewidth(13,700)#Camservo to Left
    sleep(1.5)

def cam_to_right():
    pi.set_servo_pulsewidth(13,2400)#Camservo to Right
    sleep(1.5)

move_mg(1)

#cam_to_center()
#cam_to_right()
#cam_to_left()
