//traffic light

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

S1=[27,22,23]
GPIO.setup(S1, GPIO.OUT)

S=[]
BLINK=[]
td=1
def light(S,BLINK):
    GPIO.output(S[0], BLINK[0])
    GPIO.output(S[1], BLINK[1])
    GPIO.output(S[2], BLINK[2])
    time.sleep(td)
 
while True:
   light(S1, [1,0,0])
   light(S1, [0,1,0])
   light(S1, [0,0,1])
   time.sleep(td)
