"""
created by Nagaj at 20/05/2021
"""
import time
from config import screen_setup
from snake import Snake
from food import Food
from scoreboard import Score
from constants import UP, DOWN, RIGHT, LEFT

is_game_on = True


def main():
    screen = screen_setup()
    screen.listen()
    snake = Snake()
    food = Food()
    score = Score()
    screen.onkey(key=UP, fun=snake.to_up)
    screen.onkey(key=DOWN, fun=snake.to_down)
    screen.onkey(key=RIGHT, fun=snake.to_right)
    screen.onkey(key=LEFT, fun=snake.to_left)
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.is_collision_with_food(food=food):
            score.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
