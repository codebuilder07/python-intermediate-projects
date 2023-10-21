from turtle import Turtle, Screen

screen = Screen()
starting_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.extend_snake(position)

    def extend_snake(self,position):
        new_segment = Turtle("square")
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def increase_snake_size(self):
        self.extend_snake(self.segments[-1].position())

    def direction(self):
        def move_right():
            if self.segments[0].heading() != 180:
                self.segments[0].setheading(0)
        def move_down ():
            if self.segments[0].heading() !=90:
                self.segments[0].setheading(270)
        def move_up():
            if self.segments[0].heading() != 270:
                self.segments[0].setheading(90)
        def move_left():
            if self.segments[0].heading() != 0:
                self.segments[0].setheading(180)

        screen.listen()
        screen.onkey(key="w", fun=move_up)
        screen.onkey(key="d", fun=move_right)
        screen.onkey(key="a", fun=move_left)
        screen.onkey(key="s", fun=move_down)
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)
