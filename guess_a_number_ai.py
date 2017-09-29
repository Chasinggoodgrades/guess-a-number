##########################
#Edited and perfected by:#
#       Chase P          #
##########################
import random
import time


# helper functions
def show_start_screen():
    print("HELLO")


def set_low_high():
    low = int(input("Please pick a low for the computer: "))
    high = int(input("Please pick a high for the computer: "))
    return low, high  

def show_credits():
    time.sleep(1)
    print("########################")
    print("#  HOPE YOU HAD FUN!   #")
    print("########################")
    time.sleep(1)
    print("########################")
    print("#GAME BY:CHASE(9/28/17)#")
    print("########################")
    
    
    
def get_guess(current_low, current_high):

    guess = (current_high + current_low) //2
    return guess

def pick_number():
    print()
    print("You should pick a number between " + str(low) + " and " + str(high) + ".")
    print("Press any key when you are ready to play.")
    input()
def check_guess(guess):
    answer = input("Is your number " + str(guess) + "?")
    if answer.lower() == "low" or answer.lower() == "l":
        check = -1
    elif answer.lower() == "high" or answer.lower() == "h":
        check = 1
    elif answer.lower() == "yes" or answer.lower() == "y":
        print("YAYAYAY!")
        check = 0
    else:
        print("I dont understand, please do (h,l, or y)")
        check = 2
    return check

def show_result(guess):
    print()
    print("Computer will always win. Sorry lmao")

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
    set_low_high()

    current_low = low
    current_high = high
    guess = (current_low+current_high) // 2 
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = guess + 1
            # adjust current_low
        elif check == 1:
            current_high = guess - 1
            # adjust current_high

    show_result(guess)

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
