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
# Velocidade base para camadas de background, jogadores e itens
ENTITY_SPEED = {
    'bg4_back_land': 1, 'bg4_back_decor': 2, 'bg4_battleground': 3,
    'bg4_ground_decor': 4, 'bg4_front_decor': 5, 'bg1_back_land': 1,
    'bg1_back_decor': 2, 'bg1_battleground': 3, 'bg1_ground_decor': 4,
    'bg1_front_decor': 5, 'Player1': 3, 'Player2': 3, 'Item': 2,
}

# Pontos de vida iniciais (jogadores têm fôlego/energia)
ENTITY_HEALTH = {
    'bg4_back_land': 999, 'bg4_back_decor': 999, 'bg4_battleground': 999,
    'bg4_ground_decor': 999, 'bg4_front_decor': 999, 'bg1_back_land': 999,
    'bg1_back_decor': 999, 'bg1_battleground': 999, 'bg1_ground_decor': 999,
    'bg1_front_decor': 999, 'Player1': 300, 'Player2': 300, 'Item': 1,
}

# Dano causado (não utilizado no loop atual, mas reservado para expansões)
ENTITY_DAMAGE = {
    'bg4_back_land': 0, 'bg4_back_decor': 0, 'bg4_battleground': 0,
    'bg4_ground_decor': 0, 'bg4_front_decor': 0, 'bg1_back_land': 0,
    'bg1_back_decor': 0, 'bg1_battleground': 0, 'bg1_ground_decor': 0,
    'bg1_front_decor': 0, 'Player1': 1, 'Player2': 1, 'Item': 0,
}

# Valor em pontos de cada fruta coletada
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
# Revertido para os padrões originais de movimentação e corrida
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
# Teclas de Corrida (Shift/Control) - Padrão de jogabilidade PC
PLAYER_KEY_RUN = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# --- TIMING E JOGABILIDADE ---
SPAWN_TIME = 1000  # Intervalo de surgimento das frutas (ms)
TIMEOUT_STEP = 100  # Atualização do cronômetro de fôlego/hunger (ms)
LEVEL_TIMEOUT = {'Level1': 30000, 'Level2': 60000}  # Duração base das fases

# --- DIMENSÕES DA TELA ---
WIN_WIDTH = 800
WIN_HEIGHT = 450

# --- METAS DE PONTUAÇÃO ---
LEVEL_TARGET_SCORE = {'Level1': 1500, 'Level2': 2500}

# --- BALANCEAMENTO DE DIFICULDADE ---
DIFFICULTY_LEVELS = ['Easy', 'Medium', 'Hard']
DIFFICULTY_SETTINGS = {
    'Easy':   {'time_mult': 1.5, 'goal_mult': 0.7},
    'Medium': {'time_mult': 1.0, 'goal_mult': 1.0}, # Dificuldade equilibrada original
    'Hard':   {'time_mult': 0.85, 'goal_mult': 1.35} # Modo Hard mantendo desafio real
}

# --- CORES DO HUD ---
HUD_COLOR_P1 = C_YELLOW
HUD_COLOR_P2 = C_WHITE

# --- POSICIONAMENTO DO PLACAR ---
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 100),
    'Name': (WIN_WIDTH / 2, 120),
    0: (WIN_WIDTH / 2, 110), 1: (WIN_WIDTH / 2, 130), 2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170), 4: (WIN_WIDTH / 2, 190), 5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230), 7: (WIN_WIDTH / 2, 250), 8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}