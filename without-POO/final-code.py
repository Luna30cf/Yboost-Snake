from machine import Pin
import neopixel
import time
import random

# === Initialisation matériel ===
pin = Pin(4, Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)

bRight = Pin(7, Pin.IN, Pin.PULL_UP)
bLeft = Pin(5, Pin.IN, Pin.PULL_UP)
bDown = Pin(20, Pin.IN, Pin.PULL_UP)
bUp = Pin(8, Pin.IN, Pin.PULL_UP)

# === Variables globales ===
tab = []
body = []
dir = "UP"
initBody = True
isApple = False
gameOver = False

# === Fonctions d’affichage ===
def turnOff():
    for i in range(64):
        pn[i] = (0, 0, 0)
    pn.write()

def looser():
    turnOff()
    for i in [17, 18, 19, 20, 21, 22, 25, 38, 41]:
        pn[i] = (5, 0, 0)
    pn.write()

# === Fonctions de coordonnées ===
def selectL(y):
    m = 15
    p = 1
    line = [y]
    c = y
    for i in range(3):
        y += (m - 2 * c)
        line.append(y)
        y += (p + 2 * c)
        line.append(y)
    y += (m - 2 * c)
    line.append(y)
    return line

def selectC(x):
    return [x * 8 + i for i in range(8)]

def selectCoord(x, y):
    column = selectC(x)
    line = selectL(y)
    for elementC in column:
        if elementC in line:
            return elementC

# === Contrôles et logique ===
def pomme():
    return random.randint(0, 63)

def direction():
    global dir
    if bUp.value() == 0:
        dir = "UP"
    elif bRight.value() == 0:
        dir = "RIGHT"
    elif bLeft.value() == 0:
        dir = "LEFT"
    elif bDown.value() == 0:
        dir = "DOWN"
    return dir

def move(x, y):
    if dir == "UP":
        y = 7 if y == 0 else y - 1
    elif dir == "RIGHT":
        x = 0 if x == 7 else x + 1
    elif dir == "LEFT":
        x = 7 if x == 0 else x - 1
    elif dir == "DOWN":
        y = 0 if y == 7 else y + 1
    return x, y

def wait_restart():
    print("Appuie sur un bouton pour recommencer...")
    while bUp.value() == 0 or bDown.value() == 0 or bLeft.value() == 0 or bRight.value() == 0:
        time.sleep(0.05)
    while True:
        if bUp.value() == 0 or bDown.value() == 0 or bLeft.value() == 0 or bRight.value() == 0:
            print("Bouton détecté, redémarrage...")
            time.sleep(0.2)
            break

# === Boucle principale ===
def collider():
    global initBody, isApple, gameOver

    turnOff()
    apple = pomme()
    x, y = 0, 0
    tab = [[x, y]]
    tabHead = [x, y]

    while True:
        direction()
        x, y = move(x, y)
        tabHead = [x, y]

        if initBody:
            for t in tab:
                body.append(selectCoord(t[0], t[1]))
            initBody = False

        head = body[0]

        tab.insert(0, tabHead)
        body.insert(0, selectCoord(x, y))

        if selectCoord(x, y) in body[1:]:
            gameOver = True

        if not gameOver:
            if not isApple:
                pn[body[-1]] = (0, 0, 0)
                tab.pop()
                body.pop()
                pn[apple] = (0, 5, 0)
            else:
                apple = pomme()
                isApple = False
        else:
            looser()
            wait_restart()
            return

        pn[body[0]] = (0, 5, 5)
        for segment in body[1:]:
            pn[segment] = (5, 5, 5)

        if head == apple:
            isApple = True
            pn[apple] = (0, 0, 0)

        pn.write()
        time.sleep(0.2)

# === Redémarrage automatique ===
while True:
    tab.clear()
    body.clear()
    dir = "UP"
    initBody = True
    isApple = False
    gameOver = False
    collider()
