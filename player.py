from turtle import Turtle

STARTING_POSITION = (0, -280)
SPEED = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.move_to_start()
        self.setheading(90)
        self.shape("turtle")

    def move(self):
        self.forward(SPEED)

    def move_to_start(self):
        self.goto(STARTING_POSITION)