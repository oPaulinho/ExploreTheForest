#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Const.py: Centralized game constants including colors, screen dimensions, 
event IDs, entity stats, and difficulty settings.
"""
import pygame

# --- COLOR CONSTANTS ---
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# --- EVENT IDS ---
EVENT_SPAWN = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# --- ENTITY STATISTICS ---
# Movement speed for each entity type (Background layers, Players, Items)
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

# Initial health points
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

# Damage dealt by entities
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

# Points awarded for interacting with entities
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

# --- UI & MENU ---
MENU_OPTION = ('NEW_GAME 1P',
               'NEW_GAME 2P - COOPERATIVE',
               'NEW_GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# --- PLAYER CONTROLS ---
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
# Run/Sprint keys (Shift for P2, Numeric Enter for P1)
PLAYER_KEY_RUN = {'Player1': pygame.K_KP_ENTER,
                  'Player2': pygame.K_LSHIFT}

# --- TIMING & SPAWNING ---
SPAWN_TIME = 1000  # Default fruit spawn interval in ms
TIMEOUT_STEP = 100  # 100ms refresh step for hunger/timer
LEVEL_TIMEOUT = {'Level1': 30000, 'Level2': 60000}  # Base Duration (ms)

# --- WINDOW SETTINGS ---
WIN_WIDTH = 800
WIN_HEIGHT = 450

# --- SCREEN POSITIONS ---
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

# --- GAMEPLAY GOALS ---
# Target scores to advance to next phase
LEVEL_TARGET_SCORE = {'Level1': 1500, 'Level2': 2500}

# --- DIFFICULTY SCALING ---
DIFFICULTY_LEVELS = ['Easy', 'Medium', 'Hard']
DIFFICULTY_SETTINGS = {
    'Easy':   {'time_mult': 1.5, 'goal_mult': 0.7},
    'Medium': {'time_mult': 1.0, 'goal_mult': 1.0},
    'Hard':   {'time_mult': 0.95, 'goal_mult': 1.2}
}

# --- READABILITY ---
HUD_COLOR_P1 = C_YELLOW
HUD_COLOR_P2 = C_WHITE