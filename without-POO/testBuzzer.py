from machine import Pin, PWM
import neopixel
import time
import random

# Initialisation du buzzer sur GPIO 3 (change si besoin)
buzzer = PWM(Pin(2))
buzzer.freq(1000)  # Fréquence initiale

def play_tone(frequency, duration):
    if frequency == 0:
        buzzer.duty_u16(0)  # Silence
    else:
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)  # Volume moyen

    time.sleep_ms(duration)
    buzzer.duty_u16(0)  # Stoppe le son

def play_victory_sound():
    melody = [1000, 1200, 1500, 1800, 2000]
    for note in melody:
        play_tone(note, 150)

def play_game_over_sound():
    melody = [2000, 1500, 1200, 1000, 800]
    for note in melody:
        play_tone(note, 200)

# Initialisation des LED et des boutons
pin = Pin(5, Pin.OUT)
pn = neopixel.NeoPixel(pin, 64)
bRight = Pin(4, Pin.IN, Pin.PULL_UP)
bLeft = Pin(11, Pin.IN, Pin.PULL_UP)
bDown = Pin(7, Pin.IN, Pin.PULL_UP)
bUp = Pin(6, Pin.IN, Pin.PULL_UP)

tab = []
body = []
dir = "UP"
initBody = True
isApple = False
gameOver = False

def turnOff():
    for i in range(64):
        pn[i] = (0, 0, 0)
    pn.write()

def pomme():
    return random.randint(0, 63)

def move(x, y):
    dir = direction()
    if dir == "UP":
        y = 7 if y == 0 else y - 1
    elif dir == "RIGHT":
        x = 0 if x == 7 else x + 1
    elif dir == "LEFT":
        x = 7 if x == 0 else x - 1
    elif dir == "DOWN":
        y = 0 if y == 7 else y + 1
    return x, y

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
    for elementC in range(8):
        for elementL in range(8):
            if line[elementL] == column[elementC]:
                return line[elementL]

def looser():
    turnOff()
    gameOverPattern = [17, 18, 19, 20, 21, 22, 25, 38, 41]
    for pos in gameOverPattern:
        pn[pos] = (5, 0, 0)
    pn.write()
    play_game_over_sound()  # 🔴 Son de game over

def collider():
    global initBody, isApple, gameOver
    turnOff()
    
    apple = pomme()
    x, y = 0, 0
    tab = [[x, y]]
    tabHead = [x, y]
    
    while not gameOver:
        x, y = move(x, y)
        tabHead = [x, y]

        if initBody:
            for t in tab:
                body.append(selectCoord(t[0], t[1]))
            initBody = False

        head = body[0]
        tab.insert(0, tabHead)
        body.insert(0, selectCoord(x, y))

        for i in body[1:]:
            if head == i:
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
            play_victory_sound()  # 🟢 Son quand on mange une pomme
        
        pn.write()
        time.sleep(0.2)

collider()
