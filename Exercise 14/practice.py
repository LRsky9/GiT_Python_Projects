# method - started in blocks: user input - computer random select - result definition
#added extras once basics of tge programme were up and running - attempts, intro, exit
#repeated result function to set game to 3, alot of code and messy, added boolean variable to outer while statement
#to continue the game until user quits
#variables in dict so user inputs R P or S, prefer it as a string, simpler
#save a copy without dict
#add min number of rounds
#scores after each round


import random
import sys

title = '\nLets Play...Rock, Paper, Scissor! \n'
print(title)

options = {'R': 'rock', 'P': 'paper', 'S': 'scissor'}

play_game = True

p1_wins = 0
p2_wins = 0

num_rounds = int(input("How many rounds, Playa?"))
for i in range(num_rounds):

    attempts = 1

    while attempts <= 3:
        player_1 = input('Choose wisely..:')

        if player_1 not in options:
            print('Oops! Try again')
            attempts += 1
        else:
            print('\nContender:', player_1)
            break

        if attempts > 3:
            print('Fell at the first hurdle')
            sys.exit('\nGoodbye')

    player_2 = random.randint(0, 2)


    def comp_choice(player_2):
        return options[list(options.keys())[player_2]]

    print('\nChampion:', comp_choice(player_2))


    def result(player_1, player_2, p1_wins, p2_wins):
        if (player_1 == 'rock' and options[player_2] == 'scissor') or (player_1 == 'paper' and options[player_2] == 'rock') or (player_1 == 'scissor' and options[player_2] == 'paper'):
            p1_wins += 1
            print("\nThis round to the human!")
        elif player_1 == options[player_2]:
            print('\nBore draw')
        else:
            p2_wins += 1
            print('\nAI come up trumps!')

        return p1_wins, p2_wins


if p1_wins > p2_wins:
    print('\nYou Win!')
elif p1_wins == p2_wins:
    print('\nSpoils Shared')
else:
    print('\nYou Failed, Machines Rise!')


sys.exit('\nThat was fun!')


