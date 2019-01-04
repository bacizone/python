def get_bark(weight):
    if weight > 20:
        return 'WOOOF WOOOF'
    else:
        return 'woof woof'

codies_bark = get_bark(40)
print("Codie's bark", codies_bark)

# NEW EXAMPLE
def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False
    return answer

# NEW EXAMPLE
def compute(x,y):
    total = x + y
    if (total > 10):
        total = 10
    return total

result = compute(2,3)
result = compute(11,3)

print(result)

# NEW EXAMPLE
hair = input('What color hair [brown]?')
if hair == '':
    hair = 'brown'
print('You choose', hair)

# MY PSEUDOCODE

hair = input ('What color hair')
hair_length = input ('What hair length')

person (hair, hair_length, eyes, gender, has_glasses, has beard):
name 'has' hair, hair_length, eyes, gender, has no glasses and has beard.

person_Katie ('blonde', 'long', 'blue', 'woman', 'no', 'no')