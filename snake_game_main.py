from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from  scoreboard import score
screen=Screen()
game_over_turtle=Turtle()
screen.setup(width=660,height=660)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)
snake=Snake()
food=Food()
Score=score()
starting_position=[(0,0),(-20,0),(-40,0)]
snake.direction()

game_is_on=True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        #detect collision with food
        if snake.head.distance(food)< 15:
                food.refresh()
                Score.increase_score()
                snake.increase_snake_size()


        #detect the wall collision
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
                game_is_on=False
                game_over_turtle.goto(0,0)
                game_over_turtle.color("white")
                game_over_turtle.write(f"GAME OVER",align="center",font=("ariel",36,"normal"))
        for segment in snake.segments[1:]:
                if snake.head.distance(segment)<10:
                        game_is_on= False
                        game_over_turtle.goto(0, 0)
                        game_over_turtle.color("white")
                        game_over_turtle.write(f"GAME OVER", align="center", font=("ariel", 36, "normal"))
screen.exitonclick()