#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Const.py: Centralizes global game constants. / Centraliza as constantes globais do jogo.
Manages colors, dimensions, events, stats, and difficulty settings.
Gerencia cores, dimensões, eventos, estatísticas e configurações de dificuldade.
"""
import pygame

# --- COLOR PALETTE / PALETA DE CORES ---
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# --- CUSTOM EVENTS / EVENTOS CUSTOMIZADOS ---
EVENT_SPAWN = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# --- ENTITY CONFIGURATIONS / CONFIGURAÇÕES DE ENTIDADES ---
# Base speed for background layers, players, and items / Velocidade base para camadas de fundo, jogadores e itens
ENTITY_SPEED = {
    'bg4_back_land': 1, 'bg4_back_decor': 2, 'bg4_battleground': 3,
    'bg4_ground_decor': 4, 'bg4_front_decor': 5, 'bg1_back_land': 1,
    'bg1_back_decor': 2, 'bg1_battleground': 3, 'bg1_ground_decor': 4,
    'bg1_front_decor': 5, 'Player1': 3, 'Player2': 3, 'Item': 2,
}

# Initial health points (players have stamina/energy) / Pontos de vida iniciais (jogadores têm fôlego/energia)
ENTITY_HEALTH = {
    'bg4_back_land': 999, 'bg4_back_decor': 999, 'bg4_battleground': 999,
    'bg4_ground_decor': 999, 'bg4_front_decor': 999, 'bg1_back_land': 999,
    'bg1_back_decor': 999, 'bg1_battleground': 999, 'bg1_ground_decor': 999,
    'bg1_front_decor': 999, 'Player1': 300, 'Player2': 300, 'Item': 1,
}

# Damage dealt (reserved for future expansions) / Dano causado (reservado para futuras expansões)
ENTITY_DAMAGE = {
    'bg4_back_land': 0, 'bg4_back_decor': 0, 'bg4_battleground': 0,
    'bg4_ground_decor': 0, 'bg4_front_decor': 0, 'bg1_back_land': 0,
    'bg1_back_decor': 0, 'bg1_battleground': 0, 'bg1_ground_decor': 0,
    'bg1_front_decor': 0, 'Player1': 1, 'Player2': 1, 'Item': 0,
}

# Points awarded for each fruit collected / Valor em pontos de cada fruta coletada
ENTITY_SCORE = {
    'bg4_back_land': 0, 'bg4_back_decor': 0, 'bg4_battleground': 0,
    'bg4_ground_decor': 0, 'bg4_front_decor': 0, 'bg1_back_land': 0,
    'bg1_back_decor': 0, 'bg1_battleground': 0, 'bg1_ground_decor': 0,
    'bg1_front_decor': 0, 'Player1': 0, 'Player2': 0, 'Item': 100,
}

# --- MENU AND INTERFACE / MENU E INTERFACE ---
MENU_OPTION = (
    'NEW_GAME 1P',
    'NEW_GAME 2P - COOPERATIVE',
    'NEW_GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
)

# --- PLAYER CONTROLS / CONTROLES DOS JOGADORES ---
# Reverted to original move and run keys / Revertido para os padrões originais de movimentação e corrida
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
# Sprint keys (Shift/Control) / Teclas de Corrida (Shift/Control)
PLAYER_KEY_RUN = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# --- TIMING AND GAMEPLAY / TIMING E JOGABILIDADE ---
# Restored to 3000ms to keep original challenge / Restaurado para 3000ms para manter o desafio original
SPAWN_TIME = 3000
TIMEOUT_STEP = 100
LEVEL_TIMEOUT = {'Level1': 30000, 'Level2': 60000}

# --- SCREEN DIMENSIONS / DIMENSÕES DA TELA ---
WIN_WIDTH = 800
WIN_HEIGHT = 450

# --- SCORE TARGETS / METAS DE PONTUAÇÃO ---
LEVEL_TARGET_SCORE = {'Level1': 1500, 'Level2': 2500}

# --- DIFFICULTY BALANCING / BALANCEAMENTO DE DIFICULDADE ---
DIFFICULTY_LEVELS = ['Easy', 'Medium', 'Hard']
DIFFICULTY_SETTINGS = {
    'Easy':   {'time_mult': 1.5, 'goal_mult': 0.7},
    'Medium': {'time_mult': 1.0, 'goal_mult': 1.0},
    'Hard':   {'time_mult': 0.98, 'goal_mult': 1.16}
}

# --- HUD COLORS / CORES DO HUD ---
HUD_COLOR_P1 = C_YELLOW
HUD_COLOR_P2 = C_WHITE

# --- SCOREBOARD POSITIONS / POSICIONAMENTO DO PLACAR ---
# Spacing adjusted to avoid overlapping / Espaçamento ajustado para eliminar sobreposição
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