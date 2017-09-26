import random

# config
low = 1
high = 100
import math
limit = math.ceil(math.log(high-low +1, 2))

# helper functions
def show_start_screen():
    print("┊┊┊┊┊┊┊╱▏┊┊┊┊┊┊")
    print("┊┊┊┊┊┊▕╱┊┊┊┊┊┊┊")
    print("┊┊┊╱▔▔╲┊╱▔▔╲┊┊┊")
    print("┊┊▕┈┈┈┈▔┈┈┈╱┊┊┊")
    print("┊┊▕┈┈┈┈┈┈┈┈╲┊┊┊")
    print("┊┊┊╲┈┈┈┈┈┈┈╱┊┊┊")
    print("┊┊┊┊╲▂▂▂▂▂╱┊┊┊┊")
    print()
    

def show_credits():
    print("###################################################")
    print("This game was edited and perfected by yo boy Chase.")
    print("###################################################")    
def get_guess():
    while True:
        guess = input("###Guess a number###: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print()
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
    print()
    print("You have " + str(limit) + " attempts!")
    
    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too LOW.")
    elif guess > rand:
        print("You guessed too HIGH.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
