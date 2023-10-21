import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
tim.speed('fastest')

def rnadom_colors():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color=(r,g,b)
    return random_color
gap_between_circles=5
for i in range(int(360/gap_between_circles)):
    tim.color(rnadom_colors())
    tim.circle(100)
    tim.setheading(tim.heading()+gap_between_circles)
screen=t.Screen()
screen.exitonclick()


