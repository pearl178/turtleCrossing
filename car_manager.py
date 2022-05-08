from turtle import Turtle
import random
COLORS = ['red', 'blue', 'purple', 'yellow', 'orange', 'green']
START_FREQUENCY = 8
START_SPEED = 0.1
Y_POSITION = []
n = -250
while n < 251:
    Y_POSITION.append(n)
    n += 30


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = START_SPEED
        self.possibility = START_FREQUENCY

    def create_car(self):
        MAKE_OR_NOT = random.randint(0, self.possibility)
        if MAKE_OR_NOT == 0:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            y = random.choice(Y_POSITION)
            car.color(random.choice(COLORS))
            car.pu()
            car.goto(300, y)
            self.cars.append(car)
        else:
            pass

    def move(self):
        for car in self.cars:
            car.fd(10)

    def speed_up(self):
        self.car_speed *= 0.75
        if self.possibility > 1:
            self.possibility -= 1

