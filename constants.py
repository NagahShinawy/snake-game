"""
created by Nagaj at 20/05/2021
"""

# ########  screen  #################
WIDTH = 600
HEIGHT = 600
BLACK = "black"
SCREEN_TITLE = "Snake Game"

# ########   snake    #################
SQUARE = "square"
WHITE = "white"
NORTH, SOUTH, EAST, WEST = 90, 270, 0, 180

# #########  KEYS #############
UP = "Up"
DOWN = "Down"
RIGHT = "Right"
LEFT = "Left"

# ######## FOOD  ################

CIRCLE = "circle"
BLUE = "blue"
STRETCH_LEN = STRETCH_WID = 0.5
FASTEST = "fastest"
DEFAULT_SIZE = 20
COLORS = [
    "red",
    "green",
    "blue",
    "medium slate blue",
    "purple",
    "chartreuse",
    "brown",
    "deep pink",
    "yellow",
    "white",
    "deep pink",
    "medium violet red",
    "green yellow",
    "light sky blue",
    "dark turquoise",
    "pale violet red",
    "rosy brown",
    "cyan",
    "dark orange",
    "hot pink",
    "magenta",
]

COLLISION_DISTANCE = 15  # [seg1][seg2]    [    head    ]      []
#                                                               food
# distance measured from beginning of head  <- 20px   ->


# #############  SCORE ###################

CENTER = "center"
FONT = ("Arial", 13, "bold")
SCORE_POSITION = 0, 280
SCORE_INFO = "Score : {score}, High Score: {high_score}"
GAME_OVER = "GAME OVER"

DEFAULT_POSITION = 0, 0


# ######  SAVE TO FILE ####################
DEFAULT_HIGH_SCORE = "0"
DATA = "./data"
SCORE_PATH = f"{DATA}/scores.txt"

