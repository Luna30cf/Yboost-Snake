from machine import Pin
import neopixel
import time

pin = Pin(3,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)


C1= [0,15,16,31,32,47,48,63]
L1=[0,1,2,3,4,5,6,7]

def affichage_columns():
    for i in range (8):
        L = []
        col = C1[i]
        if ((col % 2) == 0):
            for c in range (8):
                L.append(col + c)
        elif (col == 0):
            L = [0,1,2,3,4,5,6,7]
        else:
            for c in range (8):
                L.append(col - c)
        for y in range(8):
            line = L[y]
            pn[line] = (0,5,5)
            pn.write()
        time.sleep(1)
        for y in range(8):
            line = L[y]
            pn[line] = (0,0,0)
            pn.write()

def affichage_lines():
    m = 15
    p = 1
    for i in range (8):
        C = []
        line = L1[i]
        if (line == 0):
            for c in range (3):
                C.append(line + 15)
                C.append(line + 1)
            C.append(line + 15)
        for y in range(6):
            column = C[y]
            pn[column] = (0,5,5)
            pn.write()
        time.sleep(1)


affichage_lines()