# from machine import Pin
# import neopixel
# import time

# pin = Pin(3,Pin.OUT)
# pn = neopixel.NeoPixel(pin, 64)


C1= [0,15,16,31,32,47,48,63]
L1=[0,1,2,3,4,5,6,7]

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
                return line[elementL]
    return "piou"
        
print(selectCoord(3,5))