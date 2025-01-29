from machine import Pin
import neopixel
import time

pin = Pin(5,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)

class Matrice:


    C1= [0,15,16,31,32,47,48,63]
    L1=[0,1,2,3,4,5,6,7]

    def turnOff(self):
        for i in range(64):
            pn[i]=(0,0,0)
        pn.write()
    

    def affichage_columns(self):
        for i in range (8):
            L = []
            col = self.C1[i]
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

    def affichage_lines(self):
        m = 15
        p = 1
        for i in range (8):
            count = 0
            C = []
            line = self.L1[i]
            count = line
            C.append(line)
            for t in range(3):
                count = count + m
                C.append(count)
                count = count + p
                C.append(count)
            count = count + m
            C.append(count)
            m = m - 2
            p = p + 2
            for y in range(8):
                column = C[y]
                pn[column] = (5,0,5)
                pn.write()
            time.sleep(1)
            for y in range(8):
                column = C[y]
                pn[column] = (0,0,0)
                pn.write()

