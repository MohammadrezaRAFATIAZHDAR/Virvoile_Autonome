#!/usr/bin/env python

# read_PWM.py
# 2015-12-08
# Public Domain

import time
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
import read_PWM

PWM_GPIO = 12 #Pin GPIO

pi = pigpio.pi() #Cree un objet pigpio

while True:
    time.sleep(2)
    pi.set_servo_pulsewidth(PWM_GPIO, 500) # 0 degree
    time.sleep(2)
    pi.set_servo_pulsewidth(PWM_GPIO, 2500) #180 degree dans le sens horaire

pi.stop()
