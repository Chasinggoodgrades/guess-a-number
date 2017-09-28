import random

# config
low = 1
high = 100
current_low = low
current_high = high
guess = (current_low+current_high) // 2

# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):

    guess = (current_high + current_low) //2
    return guess
    
    """
    Return a truncated average of current low and high.
    """
    pass

def pick_number():
    print("You should pick a number between " + str(low) + " and " + str(high) + ".")
    print("Press any key when you are ready to play.")
    input()
def check_guess(guess):
    answer = input("Is your number " + str(guess) + "?")
    if answer in "low":
        check = -1
    elif answer in "high":
        check = 1
    elif answer in "right":
        print("YAYAYAY!")
        check = 0
    return check
    
          
          
    """
    Computer will ask if guess was too high, low, or correct.

    Returns   -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

def show_result(guess):
    print()
    print("Computer will always win. Sorry lmao")


    """
    Says the result of the game. (The computer might always win.)
    """
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
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
