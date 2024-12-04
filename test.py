from machine import Pin
import neopixel
import time

pin = Pin(5,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)
bRight = Pin(8,Pin.IN, Pin.PULL_UP)
bLeft = Pin(9,Pin.IN, Pin.PULL_UP)
bDown = Pin(7,Pin.IN, Pin.PULL_UP)
bUp = Pin(6,Pin.IN, Pin.PULL_UP)


C1= [0,15,16,31,32,47,48,63]
L1=[0,1,2,3,4,5,6,7]


def led():
    pn[55] = (0,5,5)
    pn.write()
    
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
        
def button():
    while True:
        if  bUp.value() == 1:
            pn[55] = (0,0,0)
            pn[40] = (0,5,5)
            pn.write()
        else:
            pn[40] = (0,0,0)
            pn[55] = (5,0,5)
            pn.write()
        
button()
    