from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()

screen.onkeypress(key="Up", fun=player.move)
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.update()

screen.exitonclick()