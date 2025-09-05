from turtle import Screen
from player import Player
from car import Car
from random import randint
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.colormode(255)

def generate_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

player = Player()
cars = []

screen.onkeypress(key="Up", fun=player.move)
screen.listen()

loopcount = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # generate cars
    if loopcount >= 6:
        randycord = randint(-250, 250)
        cars.append(Car(randycord, generate_color()))
        loopcount = 0

    # update cars
    for car in cars:
        car.move()
        if car.xcor() <= -320:
            cars.remove(car)

    screen.update()
    loopcount += 1

screen.exitonclick()