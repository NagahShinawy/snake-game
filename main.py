"""
created by Nagaj at 20/05/2021
"""
import time
from config import screen_setup
from snake import Snake
from constants import UP, DOWN, RIGHT, LEFT

game_isn_on = True


def main():
    screen = screen_setup()
    screen.listen()
    snake = Snake()
    screen.onkey(key=UP, fun=snake.to_up)
    screen.onkey(key=DOWN, fun=snake.to_down)
    screen.onkey(key=RIGHT, fun=snake.to_right)
    screen.onkey(key=LEFT, fun=snake.to_left)
    while game_isn_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
    screen.exitonclick()


if __name__ == "__main__":
    main()
