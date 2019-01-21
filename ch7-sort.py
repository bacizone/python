def bubble_sort(scores, numbers):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] > scores[i+1]:
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

scores = [60, 50, 58, 34, 22, 12, 67, 34, 43]

#scores = ['banana', 'apple', 'wrong', 'machine', 'depeche', 'mode', 'whole', 'zulu']

number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))

bubble_sort(scores, solution_numbers)

print('Top Bubble Solution')
for i in range(0,5):
    print(str(i+1)+')',
    'Bubble solution #' + str(solution_numbers[i]),
    'score:', scores[i])