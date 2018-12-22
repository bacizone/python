import random

winner = ''

randomChoice = random.randint(0,2)
# print(
#    'The computer chooses',
#    randomChoice)

if randomChoice == 0:
    computerChoice = 'rock'
elif randomChoice == 1:
    compterChoice = 'paper'
else:
    computerChoice = 'scissor'

# print('The computer chooses',
#      computerChoice)

userChoice = input('rock, paper or scissor?')

#print (
#    'You choose',
#   userChoice,
#    'and the computer chose',
#    computerChoice)

if computerChoice == userChoice:
    winner = 'Tie'
