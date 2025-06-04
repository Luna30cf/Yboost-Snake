from machine import Pin, PWM, ADC
import neopixel
import time
import random

# === Initialisation matériel === #
pn = neopixel.NeoPixel(Pin(4, Pin.OUT), 64)

# Initialisation des axes
vrx = ADC(Pin(2))  # X
vry = ADC(Pin(3))  # Y
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# Bouton
sw = Pin(23, Pin.IN, Pin.PULL_UP)

# Constantes
DEAD_ZONE = 500  # zone morte pour éviter les variations
CENTERX = 2400
CENTERY = 2400

# === Buzzer === #
BUZZER_PIN = 1
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0)

def play_tone(frequency, duration):
    if frequency == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(frequency)
        buzzer.duty_u16(1500)
    time.sleep_ms(duration)
    buzzer.duty_u16(0)

def play_victory_sound():
    melody = [1000, 1250, 1500]
    duration = 150
    for note in melody:
        play_tone(note, duration)
    play_tone(0, 200)

def play_game_over_sound():
    melody = [1000, 750, 500]
    duration = 200
    for note in melody:
        play_tone(note, duration)
    play_tone(0, 500)
    
def play_bomb_sound():
    melody = [1250]
    duration = 250
    for note in melody:
        play_tone(note, duration)
    play_tone(0, 500)

def play_extra_sound():
    melody = [1250,1500,1750]
    duration = 150
    for note in melody:
        play_tone(note, duration)
    play_tone(0, 500)

# === Variables globales === #
tab = []
body = []
dir = "UP"
initBody = True
isApple = False
isBomb = False
isExtra = False
bomb = None
gameOver = False
score = 0
lastDir = "UP"

# === Fonctions d’affichage === #
def turnOff():
    for i in range(64):
        pn[i] = (0, 0, 0)
    pn.write()

def looser():
    turnOff()
    for i in [17, 18, 19, 20, 21, 22, 25, 38, 41]:
        pn[i] = (5, 0, 0)
    pn.write()

def afficher_score(score):
    digits = {
        "0": [0,1,2,3,5,6,8,9,11,12,14,15,16,17],
        "1": [2,4,5,6,8,11,14,17],
        "2": [0,1,2,3,5,8,10,12,15,16,17],
        "3": [0,1,2,5,6,7,8,11,14,15,16,17],
        "4": [0,2,3,5,6,7,8,11,14,17],
        "5": [0,1,2,3,6,7,8,11,14,15,16,17],
        "6": [0,1,2,3,6,9,10,11,12,14,15,16,17],
        "7": [0,1,2,5,8,11,14,17],
        "8": [0,1,2,3,5,6,7,8,9,11,12,14,15,16,17],
        "9": [0,1,2,3,5,6,7,8,11,14,17]
    }

    bloc_gauche = [1, 14, 17, 2, 13, 18, 3, 12, 19, 4, 11, 20, 5, 10, 21, 6, 9, 22]
    bloc_droite = [33, 46, 49, 34, 45, 50, 35, 44, 51, 36, 43, 52, 37, 42, 53, 38, 41, 54]

    score_str = str(score)
    turnOff()

    if len(score_str) == 1:
        chiffre = score_str[0]
        for i in digits[chiffre]:
            pn[bloc_droite[i]] = (4, 1, 0)
    else:
        chiffre_gauche = score_str[-2]
        chiffre_droite = score_str[-1]
        for i in digits[chiffre_gauche]:
            pn[bloc_gauche[i]] = (4, 1, 0)
        for i in digits[chiffre_droite]:
            pn[bloc_droite[i]] = (4, 1, 0)

    pn.write()

# === Fonctions de coordonnées === #
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

# === Contrôles et logique === #
def pomme():
    while True:
        p = random.randint(0, 63)
        if p not in body:
            return p
def bombe():
    while True:
        b = random.randint(0, 63)
        if b not in body:
            return b
def extraP():
    while True:
        e = random.randint(0, 63)
        if e not in body:
            return e

def get_direction(x, y):
    global dir,lastDir
    
    if y < CENTERY - DEAD_ZONE:
        dir = "UP"
        lastDir= "UP"
    elif y > CENTERY + DEAD_ZONE:
        dir = "DOWN"
        lastDir = "DOWN"
    elif x < CENTERX - DEAD_ZONE:
        dir = "LEFT"
        lastDir = "LEFT"
    elif x > CENTERX + DEAD_ZONE:
        dir = "RIGHT"
        lastDir = "RIGHT"
    else :
        dir=lastDir
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
    while sw.value() == 0 :
        time.sleep(0.05)
    while True:
        if sw.value() == 0:
            print("Bouton détecté, redémarrage...")
            time.sleep(0.2)
            break

# === Boucle principale === #
def collider():
    global initBody, isApple, gameOver, score, isBomb, isExtra

    turnOff()
    score = 0
    apple = pomme()
    bomb = bombe()
    extra = extraP()
    x, y = 0, 0
    tab = [[x, y]]
    tabHead = [x, y]

    while True:
        xJ = vrx.read()
        yJ = vry.read()
        sw_val = sw.value()

        direction = get_direction(xJ, yJ)
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
            if not isBomb:
                pn[bomb] = (2, 0, 3)
            else:
                bomb = bombe()
                isBomb = False
            if not isExtra:
                pn[extra] = (3,3, 0)
            else:
                extra = extraP()
                isExtra = False
        else:
            play_game_over_sound()
            looser()
            time.sleep(1)
            afficher_score(score)
            wait_restart()
            return

        pn[body[0]] = (0, 5, 5)
        for segment in body[1:]:
            pn[segment] = (5, 5, 5)

        if head == apple and not isApple:
            isApple = True
            pn[apple] = (0, 0, 0)
            play_victory_sound()
            score += 1
            
        if head == extra and not isExtra:
            for _ in range(2): 
                body.append(body[-1]) 
                tab.append(body[-1])
            pn[extra] = (0,0,0)
            isExtra = True
            play_extra_sound()
            score += 2
        
        if head == bomb and not isBomb:
            isBomb = True
            if len(body) > 1:
                play_bomb_sound()
                pn[bomb] == (0,0,0)
                pn[body[-1]] = (0, 0, 0)
                body.pop()
                tab.pop()
            else:
                gameOver = True
                play_game_over_sound()
                looser()
                time.sleep(1)
                afficher_score(score)
                wait_restart()
                return

        pn.write()
        time.sleep(0.2)

# === Redémarrage automatique === #
while True:
    tab.clear()
    body.clear()
    dir = "UP"
    initBody = True
    isApple = False
    isBombActive = False
    gameOver = False
    score = 0
    collider()


