"""
created by Nagaj at 21/05/2021
"""
from turtle import Turtle
from constants import CENTER, FONT, WHITE, SCORE_POSITION, SCORE_INFO, GAME_OVER, DEFAULT_POSITION


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
        self.update_scoreboard(text=self.score_info.format(self.result))

    def increase_score(self):
        self.result += 1
        self.clear()
        self.update_scoreboard(text=self.score_info.format(self.result))

    def update_scoreboard(self, text):
        self.write(text, align=CENTER, font=FONT)

    def game_over(self):
        self.goto(DEFAULT_POSITION)
        self.update_scoreboard(text=GAME_OVER)
