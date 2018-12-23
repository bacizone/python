color = 'blue' #declare color variable to a color
guess = '' #initialize guess variable to an empty string
guesses = 0 # set guesses variable counter to zero

while guess != color: # repeat while loop until it is not equal to the actual color
    guess = input('What color am I thinking of?') #user inputs color
    guesses = guesses + 1 #counter increases with each non-matching color
print('You got it! It took you', guesses, 'guesses') #closes the loop and prints the number of total guesses 