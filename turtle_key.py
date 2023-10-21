import turtle
tim=turtle.Turtle()
screen=turtle.Screen()
def move_forward():
    tim.forward(10)
def move_right():
    tim.right(30)
    tim.forward(10)
def move_left():
    tim.left(30)
    tim.forward(10)
def backward():
    tim.back(10)
def exit_key():
    turtle.bye()

screen.listen()
screen.onkey(key="f",fun=move_forward)
screen.onkey(key="b",fun=backward)
screen.onkey(key="r",fun=move_right)
screen.onkey(key="l",fun=move_left)
screen.onkey(key="m",fun=exit_key)
screen.exitonclick()