from machine import Pin
import neopixel
import time
import random


pin = Pin(5,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)


class Apple:
    
    def rand():
        rand = random.randint(0, 64)
        return rand
