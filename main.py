from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Top?
    if player.ycor() > 280:
        player.back_to_start()
        scoreboard.level_up()
        car_manager.speed_up()

    # Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
