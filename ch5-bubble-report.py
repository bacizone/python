#Pseudocode for Ch5 2040 excercise
#First we have a list with solutions and their scores. We are writing a loop where it iterates until all solution -score pair are output to the screen.
#Second: using the len function we display the total number of bubble tests, that is the number of elements in the list.
#Then we need a kind of ordering algorithm, that compares the score values and select the highest. Possible solution: 1. sort the list by increasing values and select its last item (the highest) 2. always compare two values, select the highest and compare it to the next value, until there is no higher value left.
# Display the list indices assigned to the highest values - how?

scores = [60, 50, 60, 58, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

i = 0
length = len(scores)
while i < length:
    bubble_string = 'Bubble solution #'+i
    print(bubble_string, 'score:', scores[i])
    
    i = i + 1