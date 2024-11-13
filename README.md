# Snake en YBOOST

## Sommaire

- [Description](#description)
    - [1. Composants](#1-composants)
    - [2. But du jeu](#2-but-du-jeu)

## Description

### 1. Composants

ESP32-C3-Mini

Matrice Led  
    - ref Matrice : *ws2812b*  
    - ref Leds : *rgbic 5050smd*

### 2. But du jeu

Déplacer le serpent sur la matrice de led à l'aide des 4 boutons afin de manger la pomme.
Si le serpent entre en collision avec lui-même c'est un game over.
Le serpent peut "traverser" les murs.

