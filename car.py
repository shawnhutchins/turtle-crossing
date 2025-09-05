from turtle import Turtle

class Car(Turtle):

    def __init__(self, yrand, rgbcolor):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.color(rgbcolor)
        self.shapesize(1, 2)
        self.goto(320, yrand)

    def move(self):
        self.forward(10)