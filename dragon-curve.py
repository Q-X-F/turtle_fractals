import turtle
import math

Iteration = int(input("Insert number of iterations (0 = straight line): "))

if Iteration < 0:
    print("Invalid number of iterations")
    exit()

l = 512 / 2.1 ** (Iteration // 2 + 1)

turtle.penup()
turtle.speed(10)
turtle.colormode(255)

def iterate(iteration):
    if iteration == 0:
        turtle.pendown()
        turtle.forward(l)
        turtle.penup()
        turtle.back(l)
    else:
        iterate(iteration - 1)
        turtle.right((45 * iteration) % 360)
        turtle.forward(l * (math.sqrt(2) ** iteration))
        turtle.left((90 + 45 * iteration) % 360)
        iterate(iteration - 1)
        turtle.right((90 + 45 * iteration) % 360)
        turtle.back(l * (math.sqrt(2) ** iteration))
        turtle.left((45 * iteration) % 360)

turtle.setheading(90)
iterate(Iteration)
turtle.hideturtle()
turtle.done()