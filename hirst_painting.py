import turtle
import random as rand
import colorgram as color
turtle.colormode(255)
tim=turtle.Turtle()
colors = color.extract('image.jpeg',30)
color_rgb=[]
for color in colors:
    r= int(color.rgb.r)
    g = int(color.rgb.g)
    b = int(color.rgb.b)
    color_single=(r,g,b)
    color_rgb.append(color_single)
kmap=[ (212, 149, 149), (215, 80, 80), (47, 94, 94), (231, 218, 218), (148, 66, 66), (22, 27, 27), (155, 73, 73), (122, 167, 167), (40, 22, 22), (39, 19, 19), (209, 70, 70), (192, 140, 140), (39, 131, 131), (125, 179, 179), (75, 164, 164), (229, 169, 169), (15, 31, 31), (51, 55, 55), (233, 220, 220), (159, 177, 177), (99, 44, 44), (35, 164, 164), (234, 171, 171), (105, 44, 44), (164, 209, 209), (151, 206, 206)]
tim.setheading(0)
tim.penup()
tim.setpos(0,-150)
tim.speed('fastest')
dot_number =100
for i in range(1,dot_number+1):
    tim.dot(30, rand.choice(kmap))
    tim. forward(50)
    if i% 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
tim.hideturtle()







screen=turtle.Screen()
screen.exitonclick()
