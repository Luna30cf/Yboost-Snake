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
body = []
dir = "UP"
apple = None
bomb = None
isApple = False
isBombActive = False
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
def coord(x, y):
    if y % 2 == 0:
        return y * 8 + x
    else:
        return y * 8 + (7 - x)

# === Contrôles et logique ===
def get_free_position():
    while True:
        pos = random.randint(0, 63)
        if pos not in body:
            return pos

def direction(current_dir):
    if bUp.value() == 0 and current_dir != "DOWN":
        return "UP"
    elif bRight.value() == 0 and current_dir != "LEFT":
        return "RIGHT"
    elif bLeft.value() == 0 and current_dir != "RIGHT":
        return "LEFT"
    elif bDown.value() == 0 and current_dir != "UP":
        return "DOWN"
    return current_dir

def move(x, y, direction):
    if direction == "UP":
        y = 7 if y == 0 else y - 1
    elif direction == "DOWN":
        y = 0 if y == 7 else y + 1
    elif direction == "LEFT":
        x = 7 if x == 0 else x - 1
    elif direction == "RIGHT":
        x = 0 if x == 7 else x + 1
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
    global dir, apple, bomb, isApple, isBombActive, gameOver

    turnOff()
    body.clear()
    dir = "UP"
    isApple = False
    isBombActive = False
    gameOver = False

    x, y = 0, 0
    body.append(coord(x, y))
    apple = get_free_position()

    while True:
        dir = direction(dir)
        x, y = move(x, y, dir)
        head = coord(x, y)

        if head in body:
            gameOver = True
        else:
            body.insert(0, head)

            if head == apple:
                isApple = True
                apple = get_free_position()
            else:
                tail = body.pop()
                pn[tail] = (0, 0, 0)

            if not isBombActive and random.random() < 0.05:
                bomb = get_free_position()
                isBombActive = True

            if isBombActive and head == bomb:
                isBombActive = False
                pn[bomb] = (0, 0, 0)
                if len(body) > 1:
                    tail = body.pop()
                    pn[tail] = (0, 0, 0)
                else:
                    gameOver = True

        if gameOver:
            looser()
            wait_restart()
            return

        # Affichage
        for i, segment in enumerate(body):
            color = (0, 5, 5) if i == 0 else (5, 5, 5)
            pn[segment] = color

        pn[apple] = (0, 5, 0)
        if isBombActive:
            pn[bomb] = (3, 0, 2)

        pn.write()
        time.sleep(0.2)

# === Redémarrage automatique ===
while True:
    collider()
