from machine import Pin, PWM
import neopixel
import time
import random

# === Initialisation matériel === #
pn = neopixel.NeoPixel(Pin(4, Pin.OUT), 64)

# === Fonctions d’affichage === #
def turnOff():
    for i in range(64):
        pn[i] = (0, 0, 0)
    pn.write()
    
    
# === Affichage des chiffres === #
def afficher_score(score):
    digits = {
        "0": [0,1,2,3,5,6,8,9,11,12,14,15, 16, 17],
        "1": [2,4,5,6,8,11,14,17],
        "2": [0,1,2,3,5,8,10,12,15, 16,17],
        "3": [0,1,2,5,6,7,8,11,14,15, 16, 17],
        "4": [0,2,3,5,6,7,8,11,14,17],
        "5": [0,1,2,3,6,7,8,11,14,15, 16,17],
        "6": [0,1,2,3,6,9,10,11,12,14,15, 16, 17],
        "7": [0,1,2,5,8,11,14,17],
        "8": [0,1,2,3,5,6,7,8,9,11,12,14,15, 16, 17],
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


turnOff()