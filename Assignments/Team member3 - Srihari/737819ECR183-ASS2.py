import random
l=[]
a=int(input("Enter the no.of inputs: "))
for i in range(0,a):
e=int(input())
l.append(e)
print(l)
temp=random.choice(l)
hum=random.choice(l)
print(temperature,humidy)
if temperature>100:
if humidy>80:
print("MOST DANGEROUS")
else:
print("HIGH TEMPERATURE")
elif temeperature==100:
print(" no risk")
else:
print(" good")

