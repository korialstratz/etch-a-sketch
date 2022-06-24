from turtle import Turtle, Screen

timmy = Turtle()


def move():
    timmy.forward(10)


def back():
    timmy.backward(10)


def right():
    timmy.right(5)


def left():
    timmy.left(5)

def reset():
    timmy.reset()

screen = Screen()
screen.onkey(move, "Up")
screen.onkey(back, "Down")
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(reset, "c")
screen.listen()
screen.exitonclick()