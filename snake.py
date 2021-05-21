"""
created by Nagaj at 20/05/2021
"""
from turtle import Turtle
from food import Food
from constants import SQUARE, WHITE, NORTH, SOUTH, EAST, WEST, COLLISION_DISTANCE


class Snake:
    SHAPE = SQUARE
    COLOR = WHITE
    POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = NORTH
    DOWN = SOUTH
    RIGHT = EAST
    LEFT = WEST

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Snake.POSITIONS:
            segment = Turtle(shape=SQUARE)
            segment.color(WHITE)
            segment.penup()
            segment.goto(x=position[0], y=position[1])
            self.segments.append(segment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(x=new_x, y=new_y)
        self.head.forward(Snake.MOVE_DISTANCE)

    def is_collision_with_food(self, food: Food):
        if self.head.distance(food) < COLLISION_DISTANCE:
            food.move_to_random_point()

    def to_up(self):
        if self.head.heading() != Snake.DOWN:  # to prevent move versus current direction
            self.head.setheading(Snake.UP)  # to north

    def to_down(self):
        if self.head.heading() != Snake.UP:  # to prevent move versus current direction
            self.head.setheading(Snake.DOWN)  # to south

    def to_right(self):
        if self.head.heading() != Snake.LEFT:  # to prevent move versus current direction
            self.head.setheading(Snake.RIGHT)  # to east

    def to_left(self):
        if self.head.heading() != Snake.RIGHT:  # to prevent move versus current direction
            self.head.setheading(Snake.LEFT)  # to west
