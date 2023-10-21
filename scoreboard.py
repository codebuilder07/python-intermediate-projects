from turtle import Turtle
Alignment="center"
Font=("Corier",24,"normal")


class score(Turtle):
    def __init__(self):
        super().__init__()
        self.points=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.points}",align=Alignment,font=Font)

        self.hideturtle()
    def increase_score(self):
        self.points+=1
        self.clear()
        self.write(f"Score: {self.points}", align="center", font=("arial", 24, "normal"))

