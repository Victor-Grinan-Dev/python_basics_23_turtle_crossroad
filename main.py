import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

car_list = []

cap_lapse = 6
game_loop = cap_lapse
level = 1

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_loop == 0:
        game_loop = cap_lapse
        car = CarManager(level)
        car_list.append(car)

    for car in car_list:
        car.move()
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        scoreboard.level_up()
        level += 1
        cap_lapse -= 1
        player.reset_position()

    game_loop -= 1

screen.exitonclick()
