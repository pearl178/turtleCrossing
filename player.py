from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.pu()
        self.goto(STARTING_POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def back_to_start(self):
        self.goto(STARTING_POSITION)
