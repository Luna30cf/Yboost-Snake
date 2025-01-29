# Snake en YBOOST

## Timeline

- [23/10/2024](#23102024)
- [13/11/2024](#13112024)
- [4/12/2024](#4122024)

## Description

*Ce fichier contiendra les prises de notes et avancements durant ce projet Yboost consistant en la réalisation d'un Snake sur une matrice de led*
  
*Le fichier [test.py](test.py) sert à tester le fonctionnement de mon code avant de l'intégrer plus proprement aux autres fichiers. Il sera régulièrement modifié donc de nombreux fichiers (ex: [testButtons](testButtons.py), [collision](collision.py)) contiendront le code que je pense utile pour la continuité du projet*

#### **23/10/2024**

*Matin*  
Choix de l'ESP32:
- ESP32-VROOM
- ESP32-C3
- ESP32-C6

Choix de l'ESP32-VROOM car:  
plus d'expérience avec cette carte, plus de docs, plus de pins disponibles, plus de mémoire flash

Commencement de micro-python sur Thonny avec Adafruit Neopixel.
Compréhension du fonctionnement de la matrice de LED et premiers affichages lumineux

#### **13/11/2024**

Finalement passée sur ESP32-C3-Mini (expressif) par contrainte de matériel.
Pas particulièrement de changements remarqués à propos du traitement du code.

Affichage de lignes et de colonnes séparement avec [affichage.py](affichage.py)


#### **4/12/2024**

- Avancement (hors séances) avec du matériel personnel:
   
A partir de l'affichage des lignes et des colonnes, récupération de coordonnées ("tête" du serpent) [snake.py](snake.py)

- Lors de la séance:

Implémentation des boutons. [testButtons.py](testButtons.py)   
Déplacement du serpent avec les boutons. [déplacement.py](déplacement.py)   
Collision avec la pomme. [collision.py](collision.py)


#### **8/012025**

Recherche sur le tableau qui représente le snake qui s'incrémente après avoir mangé la pomme => échec voir test.py

Amélioration du déplacement avec les boutons (voir [direction.py](direction.py)):
- plus besoin d'appuyer pour se déplacer à chaque fois comme sur le fichier [déplacement.py](déplacement.py)
- rapprochement de la logique du snake

#### **29/01/2025

Tableau fonctionnel [tableau.py](tableau.py)
Achèvement du snake sans POO encore.
Début de POO

