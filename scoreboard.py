"""
created by Nagaj at 21/05/2021
"""
from turtle import Turtle
from db import read_high_score, update_high_score
from constants import (
    CENTER,
    FONT,
    WHITE,
    SCORE_POSITION,
    SCORE_INFO,
    GAME_OVER,
    DEFAULT_POSITION,
    SCORE_PATH
)


class Score(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = 0
        self.high_score = read_high_score(SCORE_PATH)
        self.score_info = SCORE_INFO
        self.create_scoreboard()

    def create_scoreboard(self) -> None:
        self.color(WHITE)
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.update_scoreboard(text=self.score_info.format(score=self.score, high_score=self.high_score))

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.update_scoreboard(text=self.score_info.format(score=self.score, high_score=self.high_score))

    def update_scoreboard(self, text) -> None:
        self.clear()
        self.write(text, align=CENTER, font=FONT)

    def game_over(self) -> None:
        self.goto(DEFAULT_POSITION)
        self.update_scoreboard(text=GAME_OVER)

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            update_high_score(path=SCORE_PATH, score=self.high_score)
            self.score = 0
        self.update_scoreboard(self.score_info.format(score=self.score, high_score=self.high_score))
