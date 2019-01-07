def drink_me(param): #drink_me is function, with 'param' as parameter 
    # here starts the function body
    msg = 'Drinking ' + param + ' glass' # msg is a variable, where we concatenate string variables with local variable 'param'
    print(msg) # we invoke function with the msg local variable as parameter
    param = 'empty' #assing string value 'empty' to param variable

glass = 'full' #'full' string is assigned to global variable glass
drink_me(glass) #invoke the drink_me function with this global variable 
print('The glass is', glass) #use print funtion with arguments inside the brackets.

