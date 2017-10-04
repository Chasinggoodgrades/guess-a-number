##########################
#Edited and perfected by:#
#       Chase P          #
##########################
import random
import time
import math




# helper functions
def show_start_screen():
    print("""             ________________$$$$
             ______________$$____$$
             ______________$$____$$
             ______________$$____$$
             ______________$$____$$
             ______________$$____$$
             __________$$$$$$____$$$$$$
             ________$$____$$____$$____$$$$
             ________$$____$$____$$____$$__$$
             $$$$$$__$$____$$____$$____$$____$$
             $$____$$$$________________$$____$$
             $$______$$______________________$$
             __$$____$$______________________$$
             ___$$$__$$______________________$$
             ____$$__________________________$$
             _____$$$________________________$$
             ______$$______________________$$$
             _______$$$____________________$$
             ________$$____________________$$
             _________$$$________________$$$
             __________$$________________$$
             __________$$$$$$$$$$$$$$$$$$$$
    """)

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

def pick_number(low, high):
    print()
    print("You should pick a number between " + str(low) + " and " + str(high) + ".")
    print("Press any key when you are ready to play.")
    input()
def check_guess(guess, tries):
    answer = input("For attempt # " + str(tries) + " is your number " + str(guess) + "? (Please use, 'l' 'h' or 'y'")
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

#Settings


def play():
    current_low,current_high = set_low_high()
    guess = (current_low+current_high) // 2     
    check = -1
    tries = 1
 
    

    
    pick_number(current_low,current_high)

    limit = math.ceil(math.log(current_high-current_low +1, 2))

    while check != 0 and tries < limit:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, tries)


        tries += 1


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
