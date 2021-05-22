game_name = str("TextRPG")






    count = 0 
    while True: 
        userName = input("Hello! Welcome to " + game_name + "! \n\n Please Login  \n\nUsername: ") 
        password = input("Password: ")
        count += 1
        if count == 3: 
            print("You've run out of attempts")
            break #exit
        else:
            if userName == 'elmo' and password == 'blue':
                print("Welcome, " + userName + " You have successfully logged in")
                break #they are in, exit loop
            else:
                #tell them it is wrong and have them retry, stay in loop
                print("Incorrect username or password, Please try again. You have " + str(3-count) + " more attempts")