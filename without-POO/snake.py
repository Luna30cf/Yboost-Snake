import time
import random

class Snake:

    def selectL(self,y):
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


    def selectC(self,x):
        column = []
        for i in range(8):
            column.append(x*8 + i)  
        return column


    def selectCoord(self,x, y):
        column = self.selectC(x)
        line = self.selectL(y)
        for elementC in range(8):
            for elementL in range(8):
                if line[elementL] == column[elementC]:
                    lum = line[elementL]
        return lum