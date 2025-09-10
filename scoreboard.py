from turtle import Turtle

LEVEL_SCOREBOARD_POS = (-220, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.goto(LEVEL_SCOREBOARD_POS)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 16, "normal"))
