import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed('fastest')
direction=[0,90,180,270]

def rnadom_colors():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color=(r,g,b)
    return random_color

for i in range(200):
    tim.color(rnadom_colors())
    tim.forward(30)
    tim.setheading(random.choice(direction))

