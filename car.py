from turtle import Turtle

CAR_SPAWN_X = 320

class Car(Turtle):

    def __init__(self, random_y, rgb_color):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.color(rgb_color)
        self.shapesize(1, 2)
        self.goto(CAR_SPAWN_X, random_y)

    def move(self, increment):
        self.forward(increment)