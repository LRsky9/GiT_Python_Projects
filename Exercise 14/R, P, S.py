import random
import sys

title = '\nLets Play...Rock, Paper, Scissor! \n'
print(title)

options = {'R': 'rock', 'P': 'paper', 'S': 'scissor'}

p1_wins = 0
p2_wins = 0

num_rounds = int(input("\nHow many rounds?"))
for i in range(num_rounds):

    attempts = 1

    while attempts <= 3:
        player_1 = input('\nChoose wisely..:')

        if player_1 not in options:
            print('\nOops! Try again')
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

        print(f"Contender: {p1_wins}  |  Champion: {p2_wins}")
        return player_1, player_2, p1_wins, p2_wins


    player_1, player_2, p1_wins, p2_wins = result(player_1, player_2, p1_wins, p2_wins)


if p1_wins > p2_wins:
    print('\nYou Win!')
elif p1_wins == p2_wins:
    print('\nSpoils Shared')
else:
    print('\nYou Failed, Machines Rise!')

print(f"\nFinal score: Contender: {p1_wins}  |  Champion: {p2_wins}")


