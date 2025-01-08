from machine import Pin
import neopixel
import time
from snake import selectCoord

pin = Pin(5,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)
bRight = Pin(4,Pin.IN, Pin.PULL_UP)
bLeft = Pin(9,Pin.IN, Pin.PULL_UP)
bDown = Pin(7,Pin.IN, Pin.PULL_UP)
bUp = Pin(6,Pin.IN, Pin.PULL_UP)


           
def move(x,y):
    while True:
        if  bUp.value() == 0:
            if y == 0:
                y = 7
            else:
                y -= 1
        if bRight.value() == 0:
            if x == 7:
                x = 0
            else :
                x += 1
        if bLeft.value() == 0:
            if x == 0:
                x = 7
            else :
                x -= 1
        if bDown.value() == 0:
            if y == 7:
                y = 0
            else :
                y += 1
        return x,y
        
