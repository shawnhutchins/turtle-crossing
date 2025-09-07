from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
from random import randint
import time

FINISH_LINE_Y = 280

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

scoreboard = Scoreboard()
player = Player()
cars = []

screen.onkeypress(key="Up", fun=player.move)
screen.listen()

loop_count = 1
car_move_increment = 10
MOVE_INCREASE = 4
game_is_on = True

while game_is_on:
    time.sleep(0.1)

    # generate cars
    if loop_count >= 6:
        random_y_cor = randint(-250, 250)
        cars.append(Car(random_y_cor, generate_color()))
        loop_count = 0

    # update cars
    for car in cars:
        car.move(car_move_increment)
        if car.xcor() <= -320:
            cars.remove(car)

    # check if the player has collided with a car
    for car in cars:
        if player.distance(car.position()) < 30 and (player.ycor() - car.ycor()) * -1 <= 20:
            game_is_on = False

    # check is player has reached the finish line
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.level += 1
        scoreboard.update_score()
        player.move_to_start()
        car_move_increment += MOVE_INCREASE

    screen.update()
    loop_count += 1

screen.exitonclick()