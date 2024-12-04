from machine import Pin
import neopixel
import time
import random

C = [0,15,16,31,33,47,48,63]
L = [0,1,2,3,4,5,6,7]


pin = Pin(5,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)

def turnOff():
    for i in range(64):
        pn[i]=(0,0,0)
    pn.write()
    
def pomme():
    for i in range(20):
        rand = random.randint(0, 64)
        pn[rand]= (0,25,0)
        pn.write()
        time.sleep(1)
        pn[rand]= (0,0,0)
        time.sleep(0.5)
        pn.write()
    pn[rand] = (0,0,0)
    pn.write()
    
pomme()
