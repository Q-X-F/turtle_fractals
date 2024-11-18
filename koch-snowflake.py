import turtle

Iteration = int(input("Enter number of iterations (0 = triangle): "))
if Iteration < 0:
    print("Invalid number of iterations")
    exit()

turtle.bgcolor("black")
turtle.color("white")
turtle.speed(10)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

def iterate(iteration):
    if iteration == 0:
        turtle.forward(512 / (3 ** (Iteration - iteration)))
    else:
        iterate(iteration - 1)
        turtle.right(60)
        iterate(iteration - 1)
        turtle.left(120)
        iterate(iteration - 1)
        turtle.right(60)
        iterate(iteration - 1)

turtle.left(60)
iterate(Iteration)
turtle.left(120)
iterate(Iteration)
turtle.left(120)
iterate(Iteration)
turtle.hideturtle()
turtle.done()