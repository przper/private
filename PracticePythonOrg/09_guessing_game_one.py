"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
    - Keep the game going until the user types “exit”
    - Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

print("Welcome to the best guessing game!")
number = random.randint(1, 10)
again = "y"
i=0
while again == "y":
    #print(number) #debug
    user_number = int(input("Please type a number from 1 to 10: "))
    if number == user_number:
        i += 1
        print("Guess number:", i)
        print("Congratulations! You guessed the number!")
        again=input("Do you want to play again? [y/n]: ")
        number = random.randint(1, 10)
        i=0
    elif number>user_number:
        i += 1
        print("Guess number:", i)
        print("Try a higher number! ")
    elif number<user_number:
        i += 1
        print("Guess number:", i)
        print("Try a lower number! ")
    else:
        print("Please type a number from 1 to 10 only.") #nie działa :/
    print(30*'-')
print("Game executed")