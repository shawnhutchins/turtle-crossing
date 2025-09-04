from turtle import Screen
from player import Player
from car import Car
from random import randint
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)

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
        cars.append(Car(randycord))
        loopcount = 0

    # update cars
    for car in cars:
        car.move()

    screen.update()
    loopcount += 1

screen.exitonclick()