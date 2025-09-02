from turtle import Turtle

SPEED = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.shape("turtle")

    def move(self):
        self.forward(SPEED)