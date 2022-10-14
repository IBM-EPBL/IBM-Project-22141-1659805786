import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

M1=[17,18,27]
GPIO.setup(M1, GPIO.OUT)

M=[]
VAL=[]
td=1
def light(M,VAL):
    GPIO.output(M[0], VAL[0])
    GPIO.output(M[1], VAL[1])
    GPIO.output(M[2], VAL[2])
    time.sleep(td)
 
while True:
   light(M1, [1,0,0])
   light(M1, [0,1,0])
   light(M1, [0,0,1])
   time.sleep(td)

