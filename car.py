from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1, 2)

    def move(self):
        self.forward(10)

    def restart(self):
        self.goto(320, self.ycor())