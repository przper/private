"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""
options = ["rock", "paper", "scissors"]  # chyba średnio pomaga
quit = "1"
print("Welcome to the best Rock, Paper, Scissors game!\n")
if input("Do you want to play? [y/n]: ") == 'y':
    while quit != "":
        print(30 * '-')
        player1 = str(input("Player 1 - please type your sign {}: ".format(options)))
        player2 = str(input("Player 2 - please type your sign {}: ".format(options)))

        if player1 == player2 and player1 in options and player2 in options:
            # print(player1==player2)
            print("A draw!")
            quit = input("To play again type anything, to stop press enter. ")

        elif player1 == options[0] and player2 == options[2]:  # rock,scissors
            print("Player 1 wins!")
            quit = input("To play again type anything, to stop press enter. ")

        elif player2 == options[0] and player1 == options[2]:  # rock,scissors
            print("Player 2 wins!")
            quit = input("To play again type anything, to stop press enter. ")

        elif player1 == options[0] and player2 == options[1]:  # rock, paper
            print("Player 2 wins!")
            quit = input("To play again type anything, to stop press enter. ")

        elif player2 == options[0] and player1 == options[1]:  # rock, paper
            print("Player 1 wins!")
            quit = input("To play again type anything, to stop press enter. ")

        elif player1 == options[1] and player2 == options[2]:  # paper, scissors
            print("Player 2 wins!")
            quit = input("To play again type anything, to stop press enter. ")

        elif player2 == options[1] and player1 == options[2]:  # paper, scissors
            print("Player 1 wins!")
            quit = input("To play again type anything, to stop press enter. ")

        else:
            print('Only {} values allowed. Please try again. '.format(options))
print(30 * '-')
print("Game executed. See you next time!")

"""
topornie ale działa

można spróbować:
elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
"""
