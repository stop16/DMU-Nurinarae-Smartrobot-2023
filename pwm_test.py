import pigpio
from time import sleep

pi = pigpio.pi()
pi.set_servo_pulsewidth(18,0)
pi.set_servo_pulsewidth(13,0)
sleep(1)

def move_mg(num):
    if num == 0:
        pi.set_servo_pulsewidth(18,1550-667)#MG996R to #1
        sleep(1)
    if num == 1:
        pi.set_servo_pulsewidth(18,1550)#MG996R to #2
        sleep(1)
    if num == 2:
        pi.set_servo_pulsewidth(18,1550+667)#MG996R to #3
        sleep(1)

def cam_to_left():
    pi.set_servo_pulsewidth(13,2400)#Camservo to Left
    sleep(1)

def cam_to_right():
    pi.set_servo_pulsewidth(13,600)#Camservo to Right
    sleep(1)

    