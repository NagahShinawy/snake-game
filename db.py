"""
created by Nagaj at 09/06/2021
"""
import os

from constants import DEFAULT_HIGH_SCORE, SCORE_PATH, DATA


def validate_path(func):
    def wrapper(path):
        if not os.path.isfile(path):
            os.mkdir(DATA)
            path = os.path.join(os.getcwd(), SCORE_PATH)
            update_high_score(path)
        return func(path)
    return wrapper


def update_high_score(path, score=DEFAULT_HIGH_SCORE):
    with open(path, "w") as f:
        f.write(str(score))


@validate_path
def read_high_score(path):
    with open(path, "r") as f:
        return int(f.read())
