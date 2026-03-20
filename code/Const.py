# C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_SPAWN = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'bg4_back_land': 1,
    'bg4_back_decor': 2,
    'bg4_battleground': 3,
    'bg4_ground_decor': 4,
    'bg4_front_decor': 5,
    'bg1_back_land': 1,
    'bg1_back_decor': 2,
    'bg1_battleground': 3,
    'bg1_ground_decor': 4,
    'bg1_front_decor': 5,
    'Player1': 3,
    'Player2': 3,
    'Item': 2,
}

ENTITY_HEALTH = {
    'bg4_back_land': 999,
    'bg4_back_decor': 999,
    'bg4_battleground': 999,
    'bg4_ground_decor': 999,
    'bg4_front_decor': 999,
    'bg1_back_land': 999,
    'bg1_back_decor': 999,
    'bg1_battleground': 999,
    'bg1_ground_decor': 999,
    'bg1_front_decor': 999,
    'Player1': 300,
    'Player2': 300,
    'Item': 1,
}

ENTITY_DAMAGE = {
    'bg4_back_land': 0,
    'bg4_back_decor': 0,
    'bg4_battleground': 0,
    'bg4_ground_decor': 0,
    'bg4_front_decor': 0,
    'bg1_back_land': 0,
    'bg1_back_decor': 0,
    'bg1_battleground': 0,
    'bg1_ground_decor': 0,
    'bg1_front_decor': 0,
    'Player1': 1,
    'Player2': 1,
    'Item': 0,
}

ENTITY_SCORE = {
    'bg4_back_land': 0,
    'bg4_back_decor': 0,
    'bg4_battleground': 0,
    'bg4_ground_decor': 0,
    'bg4_front_decor': 0,
    'bg1_back_land': 0,
    'bg1_back_decor': 0,
    'bg1_battleground': 0,
    'bg1_ground_decor': 0,
    'bg1_front_decor': 0,
    'Player1': 0,
    'Player2': 0,
    'Item': 100,
}

# M
MENU_OPTION = ('NEW_GAME 1P',
               'NEW_GAME 2P - COOPERATIVE',
               'NEW_GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# K
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_RUN = {'Player1': pygame.K_RCTRL,
                  'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100  # 100ms
LEVEL_TIMEOUT = {'Level1': 30000, 'Level2': 60000}  # Base time per level

# W
WIN_WIDTH = 800
WIN_HEIGHT = 450

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

# Target scores to advance (points per level)
LEVEL_TARGET_SCORE = {'Level1': 1500, 'Level2': 2500}

# Difficulty Settings
DIFFICULTY_LEVELS = ['Easy', 'Medium', 'Hard']
DIFFICULTY_SETTINGS = {
    'Easy':   {'time_mult': 1.5, 'goal_mult': 0.7},
    'Medium': {'time_mult': 1.0, 'goal_mult': 1.0},
    'Hard':   {'time_mult': 0.85, 'goal_mult': 1.35}
}

# HUD Colors for readability
HUD_COLOR_P1 = C_YELLOW
HUD_COLOR_P2 = C_WHITE