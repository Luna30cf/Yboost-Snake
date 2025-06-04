from machine import Pin
import neopixel
import time
import random

np = neopixel.NeoPixel(Pin(4, Pin.OUT), 64)

snake = [0, 1, 2]  # Indexs du serpent (queue à tête)
direction = 1  # va vers la droite
fruit = None
is_bomb = False
game_over = False

def turn_off():
    for i in range(64):
        np[i] = (0, 0, 0)
    np.write()

def show():
    turn_off()
    for segment in snake[:-1]:
        np[segment] = (0, 4, 4)  # Corps
    np[snake[-1]] = (0, 8, 8)   # Tête
    if fruit is not None:
        if is_bomb:
            np[fruit] = (5, 5, 5)  # Bombe : grisâtre
        else:
            np[fruit] = (0, 10, 0)  # Pomme normale
    np.write()

def get_next_head():
    head = snake[-1]
    next_head = head + direction
    # Retour ligne ?
    if next_head // 8 != head // 8:
        next_head = head - 7  # aller à la ligne suivante
    return next_head

def place_fruit():
    global fruit, is_bomb
    empty = [i for i in range(64) if i not in snake]
    fruit = random.choice(empty)
    is_bomb = random.random() < 0.3  # 30% de chance que ce soit une bombe

def move():
    global game_over
    next_head = get_next_head()

    if next_head in snake:
        print("Collision avec soi-même")
        game_over = True
        return

    snake.append(next_head)

    if next_head == fruit:
        if is_bomb:
            print("Bombe mangée !")
            if len(snake) > 1:
                snake.pop(0)  # retire un segment
            else:
                game_over = True
        else:
            print("Pomme mangée !")
        place_fruit()
    else:
        snake.pop(0)  # déplacement normal

# === INITIALISATION ===
place_fruit()
show()

# === BOUCLE DE JEU ===
while not game_over:
    move()
    show()
    time.sleep(0.5)

# === GAME OVER ===
turn_off()
for i in range(3):
    for j in snake:
        np[j] = (10, 0, 0)
    np.write()
    time.sleep(0.3)
    turn_off()
    time.sleep(0.3)
print("Game Over")
