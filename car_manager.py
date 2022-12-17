from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, level):
        super().__init__()
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(self.random_pos())
        self.setheading(180)
        self.move_speed = STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT)
        self.move()

    @staticmethod
    def random_pos():
        random_y = randint(-250, 260)
        return 320, random_y

    def move(self):
        self.forward(randint(1, self.move_speed))
