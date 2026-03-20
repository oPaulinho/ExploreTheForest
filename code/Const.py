#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Const.py: Centraliza constantes globais do jogo. 
Gerencia cores, dimensões, eventos, estatísticas e configurações de dificuldade.
"""
import pygame

# --- PALETA DE CORES ---
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# --- EVENTOS CUSTOMIZADOS ---
EVENT_SPAWN = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# --- CONFIGURAÇÕES DE ENTIDADES ---
ENTITY_SPEED = {
    'bg4_back_land': 1, 'bg4_back_decor': 2, 'bg4_battleground': 3,
    'bg4_ground_decor': 4, 'bg4_front_decor': 5, 'bg1_back_land': 1,
    'bg1_back_decor': 2, 'bg1_battleground': 3, 'bg1_ground_decor': 4,
    'bg1_front_decor': 5, 'Player1': 3, 'Player2': 3, 'Item': 2,
}

ENTITY_HEALTH = {
    'bg4_back_land': 999, 'bg4_back_decor': 999, 'bg4_battleground': 999,
    'bg4_ground_decor': 999, 'bg4_front_decor': 999, 'bg1_back_land': 999,
    'bg1_back_decor': 999, 'bg1_battleground': 999, 'bg1_ground_decor': 999,
    'bg1_front_decor': 999, 'Player1': 300, 'Player2': 300, 'Item': 1,
}

ENTITY_DAMAGE = {
    'bg4_back_land': 0, 'bg4_back_decor': 0, 'bg4_battleground': 0,
    'bg4_ground_decor': 0, 'bg4_front_decor': 0, 'bg1_back_land': 0,
    'bg1_back_decor': 0, 'bg1_battleground': 0, 'bg1_ground_decor': 0,
    'bg1_front_decor': 0, 'Player1': 1, 'Player2': 1, 'Item': 0,
}

ENTITY_SCORE = {
    'bg4_back_land': 0, 'bg4_back_decor': 0, 'bg4_battleground': 0,
    'bg4_ground_decor': 0, 'bg4_front_decor': 0, 'bg1_back_land': 0,
    'bg1_back_decor': 0, 'bg1_battleground': 0, 'bg1_ground_decor': 0,
    'bg1_front_decor': 0, 'Player1': 0, 'Player2': 0, 'Item': 100,
}

# --- MENU E INTERFACE ---
MENU_OPTION = (
    'NEW_GAME 1P',
    'NEW_GAME 2P - COOPERATIVE',
    'NEW_GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
)

# --- CONTROLES DOS JOGADORES ---
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_RUN = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# --- TIMING E JOGABILIDADE ---
SPAWN_TIME = 3000 
TIMEOUT_STEP = 100 
LEVEL_TIMEOUT = {'Level1': 30000, 'Level2': 60000}

# --- DIMENSÕES DA TELA ---
WIN_WIDTH = 800
WIN_HEIGHT = 450

# --- METAS DE PONTUAÇÃO ---
LEVEL_TARGET_SCORE = {'Level1': 1500, 'Level2': 2500}

# --- BALANCEAMENTO DE DIFICULDADE ---
DIFFICULTY_LEVELS = ['Easy', 'Medium', 'Hard']
DIFFICULTY_SETTINGS = {
    'Easy':   {'time_mult': 1.5, 'goal_mult': 0.7},
    'Medium': {'time_mult': 1.0, 'goal_mult': 1.0},
    'Hard':   {'time_mult': 0.98, 'goal_mult': 1.16} # Ajustado pelo usuário
}

# --- CORES DO HUD ---
HUD_COLOR_P1 = C_YELLOW
HUD_COLOR_P2 = C_WHITE

# --- POSICIONAMENTO DO PLACAR ---
# Vertical spacing increased to avoid overlapping (Title -> 100 -> 130 -> 160...)
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 100),
    'Label': (WIN_WIDTH / 2, 110),
    'Name': (WIN_WIDTH / 2, 150),
    0: (WIN_WIDTH / 2, 150), 1: (WIN_WIDTH / 2, 175), 2: (WIN_WIDTH / 2, 200),
    3: (WIN_WIDTH / 2, 225), 4: (WIN_WIDTH / 2, 250), 5: (WIN_WIDTH / 2, 275),
    6: (WIN_WIDTH / 2, 300), 7: (WIN_WIDTH / 2, 325), 8: (WIN_WIDTH / 2, 350),
    9: (WIN_WIDTH / 2, 375),
}