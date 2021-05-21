"""
created by Nagaj at 20/05/2021
"""
import time
from config import screen_setup
from snake import Snake
from food import Food
from scoreboard import Score
from constants import UP, DOWN, RIGHT, LEFT

# ########### ########### ##########

screen = screen_setup()
screen.listen()

# ########### ########### ##########
snake = Snake()
food = Food()
score = Score()

# ########### ########### ##########


def play():
    is_game_on = True

    screen.onkey(key=UP, fun=snake.to_up)
    screen.onkey(key=DOWN, fun=snake.to_down)
    screen.onkey(key=RIGHT, fun=snake.to_right)
    screen.onkey(key=LEFT, fun=snake.to_left)
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.is_collision_with_food(food=food):  # detect collision with food
            snake.extend()
            food.refresh()
            score.increase_score()

        if snake.is_collision_with_wall():  # detect collision with wall
            score.game_over()
            is_game_on = False
        if snake.is_collision_with_tail():
            score.game_over()
            is_game_on = False

    screen.exitonclick()


if __name__ == "__main__":
    play()