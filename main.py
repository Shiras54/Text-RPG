import json
import os
import random
import time

game_name = str("TextRPG")
base_account = {
            "id": "0",
            "username": "",
            "password": "",
            "class": "",
            "level": 1,
            "current_exp": 0,
            "next_level_exp": 10,
            "gold": 10,\
            "stat_points": 0,
            "stats": {
                "hp": 50,
                "mp": 50,
                "strength": 5,
                "endurance": 5,
                "vitality": 5,
                "magic_power": 5,
                "magic_defense": 5,
                "magic_energy": 5
            },
            "items": {
                "tier_1": {
                    "wooden_sword": {
                        "owned": False,
                        "title": "",
                        "level": 0,
                        "current_exp": 0,
                        "next_level_exp": 10,
                        "description": "",
                        "damage": 1,
                        "type": "sword",
                        "gold_value": 0,
                        "attribute": ["None", "Fire", "Water", "Earth", "Air", "Light", "Dark"]
                    },
                    "wooden_pickaxe": 0,
                    "wooden_axe": 0,
                    "wooden_hoe": 0,
                    "wooden_wand": 0
                }
            },
            "spells": {
                "tier_1": {
                    "fire_ball": {
                        "damage": 2,
                        "mana_cost": 1
                    }
                }
            }
        }

current_account = dict()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load():
    global current_account
    with open("player_db.json", "r") as player_db:
        current_account = json.load(player_db)

def save():
    global current_account
    with open("player+db.json", "w") as player_db:
        json.dump(current_account, player_db, indent=6)
    load()

def enemy(area):
    if area == 1:
        x = 1
        if x == 1:
            enemy_summoned = {
                "name": "Slime",
                "level": 1,
                "gold_value": 5,
                "exp_value": 2,
                "class": "physical",
                "stats": {
                    "hp": 10,
                    "mp": 0,
                    "strength": 1,
                    "endurance": 0,
                    "vitality": 1,
                    "magic_power": 0,
                    "magic_defense": 0,
                    "magic_energy": 0
                },
            }
            return enemy_summoned

def battle(enemy):
    global current_account
    clear()
    if enemy["class"] == "physical":
        enemy_attack = enemy["stats"]["strength"]
        enemy_defense = enemy["stats"]["endurance"]
    elif enemy["class"] == "magical":
        enemy_attack = enemy["stats"]["magic_power"]
        enemy_defense = enemy["stats"]["magic_defense"]
    elif enemy["class"] == "hybrid":
        enemy_attack = (enemy["stats"]["magic_power"] // 2) + (enemy["stats"]["strength"] // 2)
        enemy_defense = (enemy["stats"]["magic_defense"] // 2) + (enemy["stats"]["endurance"] // 2)

    if current_account["class"] == "Warrior":
        player_attack = current_account["stats"]["strength"]
        player_defense = current_account["stats"]["endurance"]
    elif current_account["class"] == "Mage":
        player_attack = current_account["stats"]["magic_power"]
        player_defense = current_account["stats"]["magic_defense"]
    elif current_account["class"] == "Spellsword":
        player_attack = (current_account["stats"]["magic_power"] // 2) + (current_account["stats"]["strength"] // 2)
        player_defense = (current_account["stats"]["magic_defense"] // 2) + (current_account["stats"]["endurance"] // 2)

    player_damage = player_attack - enemy_defense
    if player_damage <= 0:
        player_damage = 0
    enemy_damage = enemy_attack - player_defense
    if enemy_damage <= 0:
        enemy_damage = 0

    while enemy["stats"]["hp"] > 0 or current_account["stats"]["hp"] > 0:
        enemy["stats"]["hp"] = enemy["stats"]["hp"] - player_damage
        if enemy["stats"]["hp"] <= 0:
            enemy["stats"]["hp"] = 0
        if enemy["stats"]["hp"] == 0:
            print("You've defeated the [" + enemy["name"] + "], and went back to the town. After turning in the magic core to the Adventurers Guild, you got paid " + str(enemy["gold_value"]) + ". On your way back, your body healed itself completely.")
            current_account["gold"] = current_account["gold"] + enemy["gold_value"]
            current_account["stats"]["hp"] = current_account["stats"]["vitality"] * 10
            current_account["current_exp"] = current_account["current_exp"] + enemy["exp_value"]
            input("\n")
            menu()
            break
        print("You damaged the [" + enemy["name"] + "] for " + str(player_damage) + ".\n Player HP:" + str(current_account["stats"]["hp"]) + "\n" + enemy["name"] + " HP: " + str(enemy["stats"]["hp"]))
        input("\n")
        clear()

        current_account["stats"]["hp"] = current_account["stats"]["hp"] - enemy_damage
        if current_account["stats"]["hp"] <= 0:
            current_account["stats"]["hp"] = 0
        if current_account["stats"]["hp"] == 0:
            print("You've been defeated. Your has went past it's critical point and couldn't heal itself. A traveler saw you and sent you to the hospital in town, and they took 5 gold as treatment for payment.")
            current_account["gold"] = current_account["gold"] - 5
            current_account["stats"]["hp"] = current_account["stats"]["vitality"] * 10
            input("\n")
            menu()
            break
        print("The [" + enemy["name"] + "] damaged you for " + str(enemy_damage) + ".\n Player HP:" + str(current_account["stats"]["hp"]) + "\n" + enemy["name"] + " HP: " + str(enemy["stats"]["hp"]))
        input("\n")
        clear()     

def area_1():
    clear()
    enemy(1)
    enemy_summoned = enemy(1)
    print("You walk down the streets outside the town. As you're walking, you encounter a [" + enemy_summoned["name"] + "].\n")
    battle(enemy_summoned)
    

def adventure():
    print("        (1) Area 1")
    area_number = input("")
    if area_number == "1":
        area_1()

def menu():
    global current_account
    clear()
    if current_account["current_exp"] >= current_account["next_level_exp"]:
        current_account["current_exp"] = current_account["current_exp"] - current_account["next_level_exp"]
        current_account["level"] += 1
        current_account["next_level_exp"] = int(current_account["level"] * 1.5)
        current_account["stat_points"] += 3

    save()
    print(current_account["username"] + ":")
    print(" Class: " + str(current_account["class"]))
    print(" Level: " + str(current_account["level"]))
    print(" Current EXP: " + str(current_account["current_exp"]) + "/" + str(current_account["next_level_exp"]))
    print(" Gold: " + str(current_account["gold"]))
    print("\n    (1) Adventure")
    
    menu_button = input()
    if menu_button == "1":
        adventure()

def register():
    x = input("WARNING: IF YOU ALREADY HAVE A SAVE FILE, IT WILL BE DELETED TO RE-REGISTER \n ARE YOU SURE YOU WANT THIS? \n\n (y/n) \n")
    if x == "y":
        username = input("Please Register  \n\nUsername: ") 
        password = input("Password: ")
        while True:
            try:
                player_class = int(input("Select Class:\n 1) Warrior: fights using swords and maximizes physical stats. \n 2) Mage: fights using magic gloves and maximizes magical stats. \n 3) Spellsword: can use both magic gloves and swords, and use all stats but can't maximize either stats (stats are half as effective in each category.)\n"))
                break
            except gold_valueError:
                print("You haven't entered a correct gold_value")
                continue
        base_account["username"] = username
        base_account["password"] = password
        if player_class == 1: 
            base_account["class"] = "Warrior"
        elif player_class == 2:
            base_account["class"] = "Mage"
        elif player_class == 3:
            base_account["class"] = "spellsword"
        clear()

        with open("player_db.json", 'w') as player_db:
            json.dump(base_account, player_db, indent=6)
        startup()
    else: 
        startup()

def login():
    count = 0 
    try:
        with open("player_db.json", 'r') as player_db:
            playerdb = json.load(player_db)
            while True: 
                username = input("\n Please Login  \n\nUsername: ") 
                password = input("Password: ")
                count += 1
                if count == 3: 
                    print("You've run out of attempts")
                    break
                else:
                    if username == playerdb["username"] and password == playerdb["password"]:
                        print("Welcome, " + playerdb["username"] + " You have successfully logged in")
                        load()
                        clear()
                        menu()
                        break
                    else:
                        print("Incorrect username or password, Please try again. You have " + str(3-count) + " more attempts")
    except FileNotFoundError:
        register()
        
def startup():  
    x = input("Hello! Welcome to " + game_name + "! \n (1) Login  \n (2) Register  \n")
    if x == "1":
        clear()
        login()
    elif x == "2":
        clear()
        register()
    
startup()
