def play_game(my_secret_number,level):
    print("welcome to number guessing game","level","=","easy")
    print("i have selected a number btw 1 to 50.Can you guess it")

    while True:
        guess = int(input("GUESS THE NUMBER"))

        if guess == my_secret_number:
            print("CORRECT")
            break
        elif guess > my_secret_number:
            print("GUESS IS GREATER THAN MY_SECRET_NUMBER","TRY AGAIN")
        elif guess < my_secret_number:
            print("GUESS IS SMALLER THAN MY_SECRET_NUMBER","TRY AGAIN")
        else:
            print("INCORRECT")

my_secret_number_easy=35
play_game(my_secret_number_easy,"easy")

            
def play_game(my_secret_number,level):
    print("welcome to number guessing game","level","=","medium")
    print("i have selected a number btw 1 to 100.Can you guess it")

    while True:
        guess = int(input("GUESS THE NUMBER"))

        if guess == my_secret_number:
            print("CORRECT")
            break
        elif guess > my_secret_number:
            print("GUESS IS GREATER THAN MY_SECRET_NUMBER","TRY AGAIN")
        elif guess < my_secret_number:
            print("GUESS IS SMALLER THAN MY_SECRET_NUMBER","TRY AGAIN")
        else:
            print("INCORRECT")

my_secret_number_medium=90
play_game(my_secret_number_medium,"medium")

def play_game(my_secret_number,level):
    print("welcome to number guessing game","level","=","hard")
    print("i have selected a number btw 1 to 200.Can you guess it")

    while True:
        guess = int(input("GUESS THE NUMBER"))

        if guess == my_secret_number:
            print("CORRECT")
            break
        elif guess > my_secret_number:
            print("GUESS IS GREATER THAN MY_SECRET_NUMBER","TRY AGAIN")
        elif guess < my_secret_number:
            print("GUESS IS SMALLER THAN MY_SECRET_NUMBER","TRY AGAIN")
        else:
            print("INCORRECT")

my_secret_number_hard=168
play_game(my_secret_number_hard,"hard")
