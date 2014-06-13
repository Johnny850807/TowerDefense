# Screen #
SCREEN_WIDTH = 590
SCREEN_HEIGHT = 695
MARGIN = 5
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
BG_COLOR = (200, 200, 200)
O_COLOR = (100, 100, 100)
FONT = "helvetica"
FONT_SIZE = 14
FONT_COLOR = (0, 200, 0)

# Mouse Buttons #
MOUSE_LEFT = 1
MOUSE_RIGHT = 2
MOUSE_MIDDLE = 3

# enums #

## game_logic actions ##
P_IDLE = 4
P_FOLLOW = 5
P_PLACE = 6
T_SELECTED = 7
T_FIRE = 8
B_DONE = 9
B_KILL = 10
C_DEAD = 11
C_SELECTED = 12

## Sub states ##
TD_IDLE = 13
TD_FOLLOW = 14
TD_SHOW = 15

## States ##
TD_PAUSE = 16
TD_PLAYING = 17 # wave in progress
TD_CLEAR = 18 # in between waves

## Menu Buttons ##
BUTTON_NEW_WAVE_MSG = 19
BUTTON_UPGRADE_MSG = 20
BUTTON_SELL_MSG = 21

# instructions #
P_SNAP_LOC = 22

# kinds #
KIND_TOWER = 23
KIND_CREEP = 24
KIND_TILE = 25
KIND_BUTTON = 26
KIND_BULLET = 27

# Healthbar #
HEALTH_BAR_WIDTH = 20
HEALTH_BAR_HEIGHT = 5
HEALTH_BAR_BG_COLOR = (225, 0, 0)
HEALTH_BAR_COLOR = (0, 225, 0)
HEALTH_BAR_MARGIN = 3

# Menu #
MENU_O_COLOR = O_COLOR
MENU_BG_COLOR = BG_COLOR
MENU_P_X = 7
MENU_P_Y = 538
MENU_P_WIDTH = 288
MENU_P_HEIGHT = 50
MENU_B_X = 7
MENU_B_Y = 593
MENU_B_WIDTH = 288
MENU_B_HEIGHT = 77
MENU_P_O_COLOR = O_COLOR
MENU_P_BG_COLOR = BG_COLOR
MENU_B_O_COLOR = O_COLOR
MENU_B_BG_COLOR = BG_COLOR
MENU_ITEM_MARGIN_X = 10
MENU_OUTLINE_WIDTH = 3

# Display #
DISPLAY_FONT = "helvetica"
DISPLAY_FONT_SIZE = 12
DISPLAY_FONT_COLOR = (0, 0, 0)
DISPLAY_X = 300
DISPLAY_Y = 538
DISPLAY_O_COLOR = O_COLOR
DISPLAY_BG_COLOR = BG_COLOR
DISPLAY_HEIGHT = 132
DISPLAY_WIDTH = 283
DISPLAY_MARGIN_LEFT = 5
DISPLAY_MARGIN_TOP = 5
DISPLAY_NO_IMG_HEIGHT = 32
DISPLAY_NO_IMG_WIDTH = 32

# Button menu #
MENU_BUTTON_HEIGHT = 77

# Menu Buttons #
BUTTON_NEW_WAVE_IMG = "../assets/images/buttons/nextWave.png"
BUTTON_NEW_WAVE_WIDTH = 75
BUTTON_NEW_WAVE_HEIGHT = 45
BUTTON_UPGRADE_IMG = "../assets/images/buttons/upgrade.png"
BUTTON_UPGRADE_WIDTH = 75
BUTTON_UPGRADE_HEIGHT = 45
BUTTON_SELL_IMG = "../assets/images/buttons/sell.png"
BUTTON_SELL_WIDTH = 75
BUTTON_SELL_HEIGHT = 45

# Tower #
RANGE_COLOR = (50, 255, 50, 125)
RANGE_BAD_COLOR = (255, 50, 50, 125)

TOWER_BASIC_IMAGE = "../assets/images/towers/basic.png"
TOWER_BASIC_WIDTH = 32
TOWER_BASIC_HEIGHT = 32
TOWER_BASIC_COST = [25, 50, 75, 100]
TOWER_BASIC_RANGE = [70, 80, 90, 100]
TOWER_BASIC_ATK_SPEED = [2, 2.5, 2.75, 3]
TOWER_BASIC_DAMAGE = [25, 50, 100, 175]
TOWER_GREEN_IMAGE = "../assets/images/towers/green.png"
TOWER_GREEN_WIDTH = 16
TOWER_GREEN_HEIGHT = 16
TOWER_GREEN_COST = [15, 25, 35, 50]
TOWER_GREEN_RANGE = [50, 60, 70, 80]
TOWER_GREEN_ATK_SPEED = [7, 7.5, 8, 8.5]
TOWER_GREEN_DAMAGE = [8, 16, 32, 64]

# Bullet #
BULLET_BASIC_IMAGE = "../assets/images/bullets/basic.png"
BULLET_BASIC_WIDTH = 8
BULLET_BASIC_HEIGHT = 8
BULLET_BASIC_SPEED = 7
BULLET_GREEN_IMAGE = "../assets/images/bullets/green.png"
BULLET_GREEN_WIDTH = 4
BULLET_GREEN_HEIGHT = 4
BULLET_GREEN_SPEED = 7

# Money #
STARTING_MONEY = 100
MONEY_X = MARGIN
MONEY_Y = 675

# Wave #
WAVES = [[0], [10], [15], [100]]

# Creep #
CREEP_GAP = 10
CREEP_COUNT = 1
CREEP_DEFAULT_HEALTH = 100
CREEP_DEFAULT_NAME = "Red Creep"
CREEP_DEFAULT_SPEED = 2
CREEP_DEFAULT_IMAGE = "../assets/images/creeps/creep.png"
CREEP_DEFAULT_WIDTH = 16
CREEP_DEFAULT_HEIGHT = 16
CREEP_DEFAULT_VALUE = 10

# World #
WORLD_X = 7
WORLD_Y = 5
WORLD_WIDTH = 576
WORLD_HEIGHT = 528
WORLD1 = "../assets/worlds/world1.txt"
PATH_IMG = "../assets/images/tiles/path.png"
GRASS_IMG = "../assets/images/tiles/grass_outlined.png"
TILE_WIDTH = 16
TILE_HEIGHT = 16
WORLD_DEFAULT_WIDTH = 576
WORLD_DEFAULT_HEIGHT = 528
