# character = ['t', 'a', 'c', 'o']
# character = ['a', 'm', 'a', 'n', 'a', 'p', 'l','a', 'n', 'a', 'c']
character = ['w', 'a', 's', 'i', 't', 'a', 'r']

output = ''
length = len(character)

i=0
while (i < length):
    output = output + character[i]
    i = i+1

length = length * -1
i = -2

while (i >= length):
    output = output + character[i]
    i = i-1

print(output)