import turtle


IIteration = int(input("Enter number of iterations (0th = big triangle empty): "))

if IIteration < 0:
    print("Invalid number of iterations")
    exit()

turtle.bgcolor(0, 0, 0)
turtle.color(1, 1, 1)
turtle.fillcolor(1, 1, 1)
turtle.speed(10)
turtle.penup()
turtle.goto(0, 300)
turtle.pendown()
turtle.begin_fill()
turtle.right(60)
turtle.forward(512)
turtle.right(120)
turtle.forward(512)
turtle.right(120)
turtle.forward(512)
turtle.setheading(0)
turtle.end_fill()
turtle.penup()
turtle.fillcolor(0, 0, 0)


def inv_triangle(l):
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(l)
    turtle.right(120)
    turtle.forward(l)
    turtle.right(120)
    turtle.forward(l)
    turtle.setheading(0)
    turtle.end_fill()
    turtle.penup()

def iterate(iteration, Iteration):
    if iteration == 1:
        inv_triangle(256 / (2 ** (Iteration - iteration)))
    elif iteration >= 2:
        iterate(iteration - 1, Iteration)
        turtle.right(120)
        turtle.forward(256 / (2 ** (Iteration - iteration)))
        iterate(iteration - 1, Iteration)
        turtle.forward(256 / (2 ** (Iteration - iteration)))
        iterate(iteration - 1, Iteration)
        turtle.left(120)
        turtle.forward(256 / (2 ** (Iteration - iteration)))
        turtle.setheading(0)

for Iteration in range(1, IIteration + 1):
    turtle.setheading(0)
    turtle.right(120)
    turtle.forward(512 / (2 ** Iteration))
    iterate(Iteration, Iteration)
    turtle.goto(0, 300)

turtle.hideturtle()
turtle.done()


