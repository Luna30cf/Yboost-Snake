from machine import Pin
import neopixel
import time
import random


pin = Pin(5,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)


def selectL(y):
    m = 15
    p = 1
    line= [y]
    c = y
    for i in range(3):
        y += (m - 2*c)
        line.append(y)
        y += (p + 2*c)
        line.append(y)
    y += (m - 2*c)
    line.append(y)  
    return line


def selectC(x):
    column = []
    for i in range(8):
        column.append(x*8 + i)  
    return column


def selectCoord(x, y):
    column = selectC(x)
    line = selectL(y)
    for elementC in range(8):
        for elementL in range(8):
            if line[elementL] == column[elementC]:
                lum = line[elementL]
    pn[lum] = (0,5,0)
    pn.write()
    time.sleep(1)
    pn[lum]= (0,0,0)
    pn.write()
    return "piou"
        
selectCoord(2,6)