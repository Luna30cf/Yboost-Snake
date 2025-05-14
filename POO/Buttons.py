from machine import Pin


bRight = Pin(7,Pin.IN, Pin.PULL_UP)
bLeft = Pin(5,Pin.IN, Pin.PULL_UP)
bDown = Pin(20,Pin.IN, Pin.PULL_UP)
bUp = Pin(9,Pin.IN, Pin.PULL_UP)



class Buttons:
    def direction(self):
        global dir
        while True:
            if  bUp.value() == 0:
                dir = "UP"
            elif bRight.value() == 0:
                dir = "RIGHT"
            elif bLeft.value() == 0:
                dir = "LEFT"
            elif bDown.value() == 0:
                dir = "DOWN"
            return dir
        
        
    def move(self,x,y):
        dir = self.direction()
        while True:
            if  dir == "UP":
                while True:
                    if y == 0:
                        y = 7
                    else:
                        y -= 1
                    return x,y
            if dir == "RIGHT":
                while True:
                    if x == 7:
                        x = 0
                    else :
                        x += 1
                    return x,y
            if dir == "LEFT":
                while True:
                    if x == 0:
                        x = 7
                    else :
                        x -= 1
                    return x,y
            if dir == "DOWN":
                while True:
                    if y == 7:
                        y = 0
                    else :
                        y += 1
                    return x,y