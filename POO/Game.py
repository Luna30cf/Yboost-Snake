from machine import Pin
import neopixel
import time
import Buttons
import Apple
import Game
import Matrice
import Snake


pin = Pin(4,Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)
bRight = Pin(7,Pin.IN, Pin.PULL_UP)
bLeft = Pin(5,Pin.IN, Pin.PULL_UP)
bDown = Pin(20,Pin.IN, Pin.PULL_UP)
bUp = Pin(9,Pin.IN, Pin.PULL_UP)



tab = []
body = []
dir = "UP"
initBody = True
isApple = False
gameOver = False




def collider():
    global initBody
    global isApple
    
    Matrice.turnOff()
    apple = Apple.rand()
    x, y = 0,0
    tab = [[x,y]]
    tabHead = [x,y]
    
    while True:
        
        movelist = Snake.move(x, y)
        x = movelist[0]
        y = movelist[1]
        tabHead = [x,y]
        
        if initBody:
            for t in tab:
                body.append(Snake.selectCoord(t[0],t[1]))
            initBody = False
            
        head = body[0]    
        
        tab.insert(0,tabHead) 
        body.insert(0,Snake.selectCoord(x,y))
        
        i=1
        for i in body:
            if head == body[i]:
                gameOver = True
        
        if gameOver == False:
            if isApple == False: 
                pn[body[len(body)-1]]= (0,0,0) #
                tab.pop() #
                body.pop() #
                pn[apple]=(0,5,0)
                pn.write()
            else:
                apple = Apple.rand()
                isApple = False
        else:
            Matrice.looser()
        
            
        pn[body[0]]= (5,5,5)
        
        if head == apple:
            isApple = True
            pn[apple]=(0,0,0)
        
        pn.write()
        time.sleep(0.2)

collider()