"""
created by Nagaj at 21/05/2021
"""
from turtle import Turtle
from constants import CENTER, FONT, WHITE, SCORE_POSITION, SCORE_INFO


class Score(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = 0
        self.score_info = SCORE_INFO
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color(WHITE)
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.write(self.score_info.format(self.result), align=CENTER, font=FONT)

    def update(self):
        self.result += 1
        self.clear()
        self.write(self.score_info.format(self.result), align=CENTER, font=FONT)
