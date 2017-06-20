# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""


# Name: Santosh and Jeffery
# Date:


""" 
proj 03: Guessing Game
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""


#GuessingGame without Guessing

# Name: Santosh and Jeffery
# Date:


""" 
proj 03: Guessing Game
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""


#GuessingGame without Guessing

import random


magic_number = random.randint(1, 9)



start = input("\nGuess a number between 1 and 9 inclusive: ")

attempts = 0



while start != magic_number:
    if start < magic_number:
        print "You guessed too low!"
        attempts += 1
        start = input("\nEnter another number to guess: ")
    elif start > magic_number:
        print "You guessed too high!"
        attempts += 1
        start = input("\nEnter another number to guess: ")

if start == magic_number:
    print "Good job! You solved it, I guess..."
    print "You guessed it in " + str(attempts) + " attempts!"
