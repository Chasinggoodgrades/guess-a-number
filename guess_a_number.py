import random
#config
low = 1
high = 100
limit = 5
#Starting game config kinda thing
rand = random.randrange(low,high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0
#This is da actual game thingy
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

    tries += 1

if guess == rand:
    print("You win!! YAYAYAYAYAY.")
else:
    print("You're as dumb as bricks and smell like Jaden.")
    print("The actual number I was thinking of was " + str(rand) + ".")

#Making Changes
