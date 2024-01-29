import os
from random import choice


run = True
menu = True
play = False
rules = False

player_name = ""
HP = 10
ATK = 2

# clear
def clear():
    os.system("cls")

# draw line
def draw():
    print(">--------------------<")

# save func
def save():
    list = [player_name, "Health: " + str(HP), "Damage: " +  str(ATK)]
    
    with open("load.txt", 'w') as f:
        for item in list:
            f.write(f'{item}\n')

# load func
def load() -> list:
    lst = []
    with open("load.txt", 'r') as f:
        for line in f:
            lst.append(line[0:-1])  # deleting "\n" sings
    return lst    

while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()
        
        if rules:
            print("Game by Pristax 2023" + "\n" + "Rules: ")
            rules = False
            choice = ""
            
            
        choice = input("# ")
        if choice == "1":
            player_name = input("# Whats your name? ")
            menu = False
            play = True
        
        elif choice == "2":
            player_name, HP, ATK = load()
            
            clear()

            print("Welcome back " + player_name + "!", "\n" + "Player Stats: " + HP + ", ", ATK)
    
            draw()
            print("0 - SAVE AND QUIT")
            draw()

            if input() == "0":
                play = False
                menu = True
            else:
                menu = False
                play = True
            
        
        elif choice == "3":
            rules = True
        
        elif choice == "4":
            quit()
        
    while play:
        save() # autosave
        
        clear()
        draw()
        print("0 - SAVE AND QUIT")
        draw()

        destination = input("# ")
        
        if destination == "0":
            play = False
            menu = True
            save()