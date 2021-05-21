"""
created by Nagaj at 21/05/2021
"""
import random
from turtle import Turtle

from constants import (
    CIRCLE,
    COLORS,
    BLUE,
    STRETCH_LEN,
    STRETCH_WID,
    WIDTH,
    HEIGHT,
    FASTEST,
    DEFAULT_SIZE,
)


class Food(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_food()

    def create_food(self):
        self.shape(CIRCLE)
        self.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
        self.penup()
        self.color(BLUE)
        self.speed(FASTEST)
        self.move_to_random_point()

    def move_to_random_point(self):
        random_x = random.randint(
            (-WIDTH // 2) + DEFAULT_SIZE, (WIDTH // 2) - DEFAULT_SIZE
        )  # -280 to 280
        random_y = random.randint(
            (-HEIGHT // 2) + DEFAULT_SIZE, (HEIGHT // 2) - DEFAULT_SIZE
        )  # -280 to 280
        self.goto(random_x, random_y)

    def refresh(self):
        self.color(random.choice(COLORS))
        self.move_to_random_point()
