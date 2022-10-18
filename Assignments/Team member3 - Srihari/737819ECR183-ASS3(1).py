import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

H1=[20,26,21]
GPIO.setup(H1, GPIO.OUT)

H=[]
NUM=[]
td=1
def light(H,NUM):
    GPIO.output(H[0], NUM[0])
    GPIO.output(H[1], NUM[1])
    GPIO.output(H[2], NUM[2])
    time.sleep(td)
 
while True:
   light(H1, [1,0,0])
   light(H1, [0,1,0])
   light(H1, [0,0,1])
   time.sleep(td)

