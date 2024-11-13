from machine import Pin
import neopixel
import time

pin = Pin(3,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)

C = [0,15,16,31,32,47,48,63]
L = [0,1,2,3,4,5,6,7]
def affichage():
    for i in range (8):
        col = C[i]
        line = L[i]
        pn[col] = (25,0,25)
        pn[line] = (0,25,25)
        pn.write()
        time.sleep(0.3)
        pn[col] = (0,0,0)
        pn[line] = (0,0,0)
        pn.write()

affichage()