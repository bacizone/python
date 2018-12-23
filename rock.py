# import random package and initialize a winner variable with an empty string

import random

winner = ''

# random method select a random number between 0 and 2 and assigns it to the randomChoice variable
randomChoice = random.randint(0,2)

# randomChoice values assign string to computerChoice
if randomChoice == 0:
    computerChoice = 'rock'
elif randomChoice == 1:
    computerChoice = 'paper'
else:
    computerChoice = 'scissor'

userChoice = '' # set variable to empty string
while (userChoice != 'rock' and #why and and not or??? 
      userChoice != 'paper' and
      userChoice != 'scissors'):
    userChoice = input('rock, paper or scissors? ')

# evaluates the case when computer and the user choose the same
if computerChoice == userChoice:
    winner = 'Tie'

# evaluates the cases where computer wins, otherwise user wins.
elif computerChoice == 'paper' and userChoice == 'rock':
    winner = 'Computer'
elif computerChoice == 'rock' and userChoice == 'scissors':
    winner = 'Computer'
elif computerChoice == 'scissors' and userChoice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# prints the message in case of Tie
if winner == 'Tie':
    print('We both chose', computerChoice, 'play again!')
# print who won the game
else:
    print(winner, 'won, I chose', computerChoice, '.')