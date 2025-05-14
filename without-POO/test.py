from machine import Pin
import neopixel
import time
import random

# from déplacement import move
# from snake import selectCoord
# from affichage import turnOff



pin = Pin(4,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)
bRight = Pin(7,Pin.IN, Pin.PULL_UP)
bLeft = Pin(5,Pin.IN, Pin.PULL_UP)
bDown = Pin(20,Pin.IN, Pin.PULL_UP)
bUp = Pin(8,Pin.IN, Pin.PULL_UP)



tab = []
body = []
dir = "UP"
initBody = True
isApple = False
gameOver = False

def turnOff():
    for i in range(64):
        pn[i]=(0,0,0)
    pn.write()

def pomme():
    while True:
        rand = random.randint(0, 64)
        return rand
    
    
def move(x,y):
    dir = direction()
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
    
def direction():
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
    return lum

def looser():
    turnOff()
    pn[17] = (5,0,0)
    pn[18] = (5,0,0)
    pn[19] = (5,0,0)
    pn[20] = (5,0,0)
    pn[21] = (5,0,0)
    pn[22] = (5,0,0)
    pn[25] = (5,0,0)
    pn[38] = (5,0,0)
    pn[41] = (5,0,0)
    pn.write()
        
 
def collider():
    global initBody
    global isApple
    global gameOver
    
    turnOff()
    apple = pomme()
    x, y = 0, 0
    tab = [[x, y]]
    tabHead = [x, y]
    
    while True:
        movelist = move(x, y)
        x = movelist[0]
        y = movelist[1]
        tabHead = [x, y]
        
        if initBody:
            for t in tab:
                body.append(selectCoord(t[0], t[1]))
            initBody = False
        
        head = body[0]    
        
        tab.insert(0, tabHead) 
        body.insert(0, selectCoord(x, y))
        
        # ✅ Collision avec soi-même
        if selectCoord(x, y) in body[1:]:
            gameOver = True
        
        if not gameOver:
            if not isApple: 
                pn[body[-1]] = (0, 0, 0)
                tab.pop()
                body.pop()
                pn[apple] = (0, 5, 0)
                pn.write()
            else:
                apple = pomme()
                isApple = False
        else:
            looser()
        
        pn[body[0]] = (5, 5, 5)
        
        if head == apple:
            isApple = True
            pn[apple] = (0, 0, 0)
        
        pn.write()
        time.sleep(0.2)
        
turnOff()