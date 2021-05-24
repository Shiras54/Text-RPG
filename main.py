import json
import os

game_name = str("TextRPG")
base_account = {
            "id": "0",
            "username": "",
            "password": "",
            "level": 1,
            "current_exp": 0,
            "next_level_exp": 10,
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
                        "value": 0,
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

                }
            }
        }

current_account = dict()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save():
    with open("player+db.json", "w") as player_db:
        json.dump(current_account, player_db, indent=6)

def load():
    global current_account
    with open("player_db.json", "r") as player_db:
        current_account = json.load(player_db)

def menu():
    global current_account
    print("Welcome to " + game_name + '.')
    print(current_account["username"] + ":")
    print(" Level: " + str(current_account["level"]))
    print(" Current EXP: " + str(current_account["current_exp"]))
    print(" Level Up EXP: " + str(current_account["next_level_exp"]))
    print()

    save()
    input()

def register():
    x = input("WARNING: IF YOU ALREADY HAVE A SAVE FILE, IT WILL BE DELETED TO RE-REGISTER \n ARE YOU SURE YOU WANT THIS? \n\n (y/n) \n")
    if x == "y":
        username = input("Please Register  \n\nUsername: ") 
        password = input("Password: ")
        
        base_account["username"] = username
        base_account["password"] = password
        
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
        login()
    if x == "2":
        register()
    
startup()
