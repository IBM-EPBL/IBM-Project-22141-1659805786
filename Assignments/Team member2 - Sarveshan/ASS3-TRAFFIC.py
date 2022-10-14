//traffic light

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

A1=[24,25,17]
GPIO.setup(A1, GPIO.OUT)

A=[]
TRAFFIC=[]
td=1
def light(M,VAL):
    GPIO.output(A[0], TRAFFIC[0])
    GPIO.output(A[1], TRAFFIC[1])
    GPIO.output(A[2], TRAFFIC[2])
    time.sleep(td)
 
while True:
   light(A1, [1,0,0])
   light(A1, [0,1,0])
   light(A1, [0,0,1])
   time.sleep(td)
