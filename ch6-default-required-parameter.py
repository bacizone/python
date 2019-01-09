# Required parameter demonstration
def greet(name, emoticon, message='You rule!'):
    print('Hi', name + '.', message, emoticon)

#greet('John',)
greet('Jenny', 'How are you today?')
greet(message='Where have you been?', name='Jill', emoticon='thumbs up')

