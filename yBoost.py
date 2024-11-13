from machine import Pin
import neopixel
import time
import random


pin = Pin(3,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)

def pomme():
    for i in range(20):
        rand = random.randint(0, 63)
        pn[rand]= (0,25,0)
        pn.write()
        time.sleep(1)
        pn[rand]= (0,0,0)
        time.sleep(0.5)
        pn.write()
    pn[rand] = (0,0,0)
    pn.write()
    
pomme()

