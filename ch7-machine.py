# Using Python builtin sorting algorithm
# scores = [3, 5, 3, 7, 9, 5,676, 454, 2986, 13, 34, 64, 4, 6]

# # def sort(scores): - but you do not need to define sorting function this time, as you are using the built in fucntion of Python. 

# scores.sort(reverse=True)
# print(scores)

character = 'taco'
character = 'amanaplanac'
character = 'wasitar'

output = ''
length = len(character)
i=0
while (i < length):
    output = output + character[i]
    i = i + 1

length = length * -1
i = -2

while (i >= length):
    output = output + character[i]
    i = i - 1

print(output)