//TRAFFIC LIGHT FOR 4 WAYS

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

M1=[12,6,5]
M2=[24,23,22]
M3=[27,18,17]
M4=[19,16,13]

GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M3, GPIO.OUT)
GPIO.setup(M4, GPIO.OUT)

M=[]
VAL=[]
td=1.5
t1=1
t2=0.1
def light(M,VAL):
    GPIO.output(M[0], VAL[0])
    GPIO.output(M[1], VAL[1])
    GPIO.output(M[2], VAL[2])
 
while True:
   light(M1, [1,0,0])    
   light(M2, [0,0,1])
   light(M3, [0,0,1])
   light(M4, [0,0,1])
   time.sleep(td)
   light(M1, [1,1,0])
   light(M2, [0,1,1])
   light(M3, [0,0,1])
   light(M4, [0,0,1])
   time.sleep(t1)
   light(M1, [0,0,0])
   light(M2, [0,0,0])
   light(M3, [0,0,0])
   light(M4, [0,0,0])
   time.sleep(t2)
    
   light(M1, [0,0,1])	  
   light(M2, [1,0,0])
   light(M3, [0,0,1])
   light(M4, [0,0,1])
   time.sleep(td)
   light(M1, [0,0,1])
   light(M2, [1,1,0])
   light(M3, [0,1,1])
   light(M4, [0,0,1])
   time.sleep(t1)
   light(M1, [0,0,0])
   light(M2, [0,0,0])
   light(M3, [0,0,0])
   light(M4, [0,0,0])
   time.sleep(t2)
    
   light(M1, [0,0,1])     
   light(M2, [0,0,1])
   light(M3, [1,0,0])
   light(M4, [0,0,1])
   time.sleep(td)
   light(M1, [0,0,1])
   light(M2, [0,0,1])
   light(M3, [1,1,0])
   light(M4, [0,1,1])
   time.sleep(t1)
   light(M1, [0,0,0])
   light(M2, [0,0,0])
   light(M3, [0,0,0])
   light(M4, [0,0,0])
   time.sleep(t2)
   
   light(M1, [0,0,1])      
   light(M2, [0,0,1])
   light(M3, [0,0,1])
   light(M4, [1,0,0])
   time.sleep(td)
   light(M1, [0,1,1])
   light(M2, [0,0,1])
   light(M3, [0,0,1])
   light(M4, [1,1,0])
   time.sleep(t1)
   light(M1, [0,0,0])
   light(M2, [0,0,0])
   light(M3, [0,0,0])
   light(M4, [0,0,0])
   time.sleep(t2)
