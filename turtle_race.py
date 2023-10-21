from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","blue","pink","black","green"]
locations=[-70,-40,-10,20,50]
all_turtles=[]
for tutle in range(0,5):
    tim= Turtle(shape="turtle")
    tim.color(colors[tutle])
    tim.penup()
    tim.goto(x=-230,y=locations[tutle])
    all_turtles.append(tim)


game_on=True
while game_on:
    for turtle in all_turtles:
        if turtle.xcor()>=230:
            game_on=False
            print(f'Winner is {turtle.pencolor()}. ')
        rand=random.randint(0,10)
        turtle.forward(rand)

screen.exitonclick()