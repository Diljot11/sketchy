from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_for():
    tim.forward(10)


def rotate_clockwise():
    tim.right(10)


def rotate_anti():
    tim.left(10)


def move_back():
    tim.back(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_for, 'w')

screen.onkey(rotate_clockwise, 'd')
screen.onkey(rotate_anti, 'a')
screen.onkey(move_back, 's')
screen.onkey(clear,'c')
screen.exitonclick()
