import json
import os

game_name = str("TextRPG")
base_account = {
            "id": "0",
            "username": "",
            "password": "",
            "level": 1
        }

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def register():
    x = input("WARNING: IF YOU ALREADY HAVE A SAVE FILE, IT WILL BE DELETED TO RE-REGISTER \n ARE YOU SURE YOU WANT THIS? \n\n (y/n) \n")
    if x == "y":
        username = input("Please Register  \n\nUsername: ") 
        password = input("Password: ")
        
        base_account["username"] = username
        base_account["password"] = password
        
        clear()

        with open("player_db.json", 'w') as player_db:
            json.dump(base_account, player_db, indent=4)
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
                        clear()
                        menu()
                        break
                    else:
                        print("Incorrect username or password, Please try again. You have " + str(3-count) + " more attempts")
    except FileNotFoundError:
        register()
        

def menu():
    with open("player_db.json", "r") as player_db:
        playerdb = json.load(player_db)
    print("Welcome to " + game_name + '.')
    print(playerdb["username"] + ": \n Level " + playerdb["level"] )
    input("")

def startup():
    x = input("Hello! Welcome to " + game_name + "! \n (1) Login  \n (2) Register  \n")
    if x == "1":
        login()
    if x == "2":
        register()
    
startup()
