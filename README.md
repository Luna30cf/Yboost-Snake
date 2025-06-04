# Snake en YBOOST

## Sommaire

- [Description](#description)
    - [1. Composants](#1-composants)
    - [2. But du jeu](#2-but-du-jeu)
    - [3. Features](#3-features)
    - [4. Avancement](#4-avancement)
    - [5. Arborescence](#5-arborescence)

## Description

### 1. Composants

ESP32-C3-Mini

Matrice Led  
    - ref Matrice : *ws2812b*  
    - ref Leds : *rgbic 5050smd*
    - ref Carte : *ESP32-C6*

### 2. But du jeu

Déplacer le serpent sur la matrice de led à l'aide des 4 boutons ou du joystick afin de manger la pomme.
Si le serpent entre en collision avec lui-même c'est un game over.
Le serpent peut "traverser" les murs (bords de la matrice).

### 3. Features

Si le serpent mange une pomme violette, il rétrécit d'une case. Attention s'il faisait déjà qu'une seule case, il disparaît et c'est game over.

Si le serpent mange une pomme jaune, il grandit de deux cases. Attention à pas devenir trop grand et se manger.

Lors d'un game over, un énorme L apparait durant quelques secondes siginfiant "LOOSER", puis le score s'affiche jusqu'au lancement d'une nouvelle partie en appuyant sur le joystick.

### 4. Avancement 

Le fichier [Avancement](Avancement.md) relate, comme son nom l'indique, l'avancement du projet au fil des séances et même hors séances.
Il aide à la compréhension des divers fichiers et à la logique employé.
Je l'utiliserai comme aide pour préparer le support de présentation du projet fini. 


### 5. Arborescence

- Dossier ["Without-POO"](/without-POO/) ➡️ codes fonctionnels, différents tests de ma part
- Dossier [POO](/POO/) ➡️ pas le temps de passer en POO, trop complexe, mais tests pas fonctionnels malgré tout
- Dossiers et autres fichiers ci-dessous ➡️ Création PCB sur Altium Designer
    - [Previews](/__Previews/), [Gerber](/Gerber/), [Gerber.zip](/Gerber.zip),[NC Drill](/NC%20Drill/)
    - [PCB1](PCB1.PcbDoc), [PCBlib](PcbLib1.PcbLib), [schéma Doc](schéma.SchDoc), [schéma lib](Schlib1.SchLib), [schéma PDF](schéma.PDF)
