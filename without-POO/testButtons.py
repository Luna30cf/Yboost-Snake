from machine import Pin
import time

bRight = Pin(8,Pin.IN, Pin.PULL_UP)
bLeft = Pin(9,Pin.IN, Pin.PULL_UP)
bDown = Pin(7,Pin.IN, Pin.PULL_UP)
bUp = Pin(6,Pin.IN, Pin.PULL_UP)

def testRbutton():
    while True:
        if bRight.value() == 1:
            print("value bRight = 1")
            time.sleep(2)
        else:
            print("value bRight = 0")
            time.sleep(2)
def testLbutton():
    while True:
        if bLeft.value() == 1:
            print("value bLeft = 1")
            time.sleep(2)
        else:
            print("value bLeft = 0")
            time.sleep(2)
        
def testUbutton():
    while True:
        if bUp.value() == 1:
            print("value bUp = 1")
            time.sleep(2)
        else:
            print("value bUp = 0")
            time.sleep(2)
        
def testDbutton():
    while True:
        if bDown.value() == 1:
            print("value bDown = 1")
            time.sleep(2)
        else:
            print("value bDown = 0")
            time.sleep(2)


testDbutton()