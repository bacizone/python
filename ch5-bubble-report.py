#Pseudocode for Ch5 2040 excercise
#First we have a list with solutions and their scores. We are writing a loop where it iterates until all solution -score pair are output to the screen.
#Second: using the len function we display the total number of bubble tests, that is the number of elements in the list.
#Then we need a kind of ordering algorithm, that compares the score values and select the highest. Possible solution: 1. sort the list by increasing values and select its last item (the highest) 2. always compare two values, select the highest and compare it to the next value, until there is no higher value left.
# Display the list indices assigned to the highest values - how?

scores = [60, 50, 60, 58, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .33, .31, .25, .29, .27, .22, .31, .25, .25, .33, .21, .25, .25, .25, .28, .25, .24, .22, .20, .25, .30, .25, .24, .25, .25, .25, .27, .25, .26, .29]

# i = 0
length = len(scores)
high_score = 0
# this was a less efficient method
# while i < length:
#     bubble_string = 'Bubble solution #'+ str(i)
#     print(bubble_string, 'score:', scores[i])
# i = i + 1

for i in range(length):
    bubble_string = 'Bubble solution #'+ str(i)
    print(bubble_string, 'score:', scores[i])

    if scores[i] > high_score:
        high_score = scores[i]

print('Bubble test:', length) 
print('Highest bubble score:', high_score)

# best_solutions = []
# if scores[i] == high_score:
#     for j in range(high_score):
#         best_solutions.append(high_score)

best_solutions = []
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)

print('Solutions with highest score:', best_solutions)

cost = 100.0
most_effective = 0
for i in range(length):
    if scores[i] == high_score and costs[i] < cost:
        most_effective = i
        cost = costs[i]
print('Solution', most_effective, 'is the most effective with a cost of', costs[most_effective])

