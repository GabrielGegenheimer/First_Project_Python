import os
import platform # Para identificar o sistema operacional
import time # Para monitorar as teclas pressionadas
import keyboard  # Para monitorar as teclas pressionadas

player = {"name": "python", "x": 0, "y": 0}
map_width = 10
map_height = 5

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def walk(direction):
    if direction == "d" and player['x'] < map_width - 1:
        player['x'] += 1
    elif direction == "a" and player['x'] > 0:
        player['x'] -= 1
    elif direction == "w" and player['y'] > 0:
        player['y'] -= 1
    elif direction == "s" and player['y'] < map_height - 1:
        player['y'] += 1

while True:
    clear_screen()

    print("-------------------------")

    for y in range(map_height):
        print("\n")
        for x in range(map_width):
            if player['x'] == x and player['y'] == y:
                print("🤺", end="")
            else:
                print("🟩", end="")
    print("\n")
    print("--------------------------")
    print("next direction (w,a,s,d): ")

    key = keyboard.read_key()

    if key in ['w', 'a', 's', 'd']:
        walk(key)

    time.sleep(0.1)

'''  # Verifica se alguma das teclas de direção foi pressionada
    if keyboard.is_pressed('w'):
        walk("w")
    elif keyboard.is_pressed('a'):
        walk("a")
    elif keyboard.is_pressed('s'):
        walk("s")
    elif keyboard.is_pressed('d'):
        walk("d")
    
    # Aguarda um pequeno tempo para não sobrecarregar o loop
    os.system('sleep 0.1') '''


