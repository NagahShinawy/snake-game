"""
created by Nagaj at 09/06/2021
"""
import os

from constants import DEFAULT_HIGH_SCORE


def create_scores_dir_if_not_exist(path) -> bool:
    if os.path.isfile(path):
        return True
    os.mkdir("scores")


def update_high_score(path, score=DEFAULT_HIGH_SCORE):
    with open(path, "w") as f:
        f.write(str(score))


def _get_high_score(path):
    with open(path, "r") as f:
        return int(f.read())


def get_updated_high_score(path):
    if create_scores_dir_if_not_exist(path) is None:
        update_high_score(path)
    return _get_high_score(path)
