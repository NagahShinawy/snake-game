"""
created by Nagaj at 20/05/2021
"""
from turtle import Turtle

from constants import SQUARE, WHITE, NORTH, SOUTH, EAST, WEST, COLLISION_DISTANCE
from food import Food


class Snake:
    """
    handle snake operation, create, move, extend, collision
    """
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

    def create_snake(self) -> None:
        """
        create 3 snake segments at first
        :return:
        """
        for position in Snake.POSITIONS:
            self.add_segment(position)

    def move(self) -> None:
        """
        move snake segments
        :return:
        """
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(x=new_x, y=new_y)
        self.head.forward(Snake.MOVE_DISTANCE)

    def add_segment(self, position, color=WHITE) -> None:
        """
        add segment to the snake [to the end of snake] [to the tail]
        :param position: segment's position
        :param color: segment's color
        :return:
        """
        segment = Turtle(shape=SQUARE)
        segment.color(color)
        segment.penup()
        segment.goto(*position)
        self.segments.append(segment)

    def extend_and_refresh_color(self, color) -> None:
        self.add_segment(self.segments[-1].position(), color)

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())

    def is_collision_with_food(self, food: Food) -> bool:
        return self.head.distance(food) < COLLISION_DISTANCE

    def is_collision_with_wall(self) -> bool:
        is_touch_wall = [
            self.head.xcor() > 280,
            self.head.xcor() < -280,
            self.head.ycor() > 280,
            self.head.ycor() < -280,
        ]
        return any(is_touch_wall)

    def is_collision_with_tail(self) -> bool:
        for segment in self.segments[
            1:
        ]:  # slicing to avoid head to touch it self at first iteration,
            # because first segment is the head
            # if segment == self.head:
            #     continue
            if self.head.distance(segment) < 10:
                return True
        return False

    def to_up(self) -> None:
        if (
            self.head.heading() != Snake.DOWN
        ):  # to prevent move versus current direction
            self.head.setheading(Snake.UP)  # to north

    def to_down(self) -> None:
        if self.head.heading() != Snake.UP:  # to prevent move versus current direction
            self.head.setheading(Snake.DOWN)  # to south

    def to_right(self) -> None:
        if (
            self.head.heading() != Snake.LEFT
        ):  # to prevent move versus current direction
            self.head.setheading(Snake.RIGHT)  # to east

    def to_left(self) -> None:
        if (
            self.head.heading() != Snake.RIGHT
        ):  # to prevent move versus current direction
            self.head.setheading(Snake.LEFT)  # to west

    def reset(self):
        self.hide()
        self.__init__()

    def hide(self):
        for segment in self.segments:
            segment.hideturtle()
            # segment.goto(1000, 1000)  # go way out of screen
