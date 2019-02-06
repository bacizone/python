import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')
pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')

slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(50)

slowpoke.pencolor('red')
slowpoke.penup()
slowpoke.setposition(120, 0)
slowpoke.pendown()
slowpoke.circle(50)

# def make_square(the_turtle):
#     for i in range(0,4):
#         the_turtle.forward(100)
#         the_turtle.right(90)

def make_spiral(the_turtle):
    # for i in range(0, 36):
    #     make_square(the_turtle)
    #     the_turtle.right(10)

    for i in range(5):
        slowpoke.forward(100)
        slowpoke.right(144)

def make_shape(t, sides):
    angle = 360/sides
    for i in range(0, sides):
        t.forward(100)
        t.right(angle)

make_shape(slowpoke, 3)
make_shape(slowpoke, 5)
make_shape(slowpoke, 8)
make_shape(slowpoke, 10)



# make_square(slowpoke)
# pokey.right(45)
# make_square(pokey)

make_spiral(slowpoke)
pokey.right(5)
make_spiral(pokey)

turtle.mainloop()
