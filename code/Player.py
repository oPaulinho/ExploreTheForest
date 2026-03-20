#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Player.py: Implementação dos personagens jogáveis.
Especializa Entity para suportar animação por frames e movimentação por teclado.
"""
import pygame
from code.Const import (
    ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_RIGHT, 
    PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, PLAYER_KEY_RUN
)
from code.Entity import Entity


class Player(Entity):
    """Entidade controlada pelo usuário com sistema de animação e estados."""

    def __init__(self, name: str, position: tuple):
        """
        Inicializa o jogador chamando a base e configurando as folhas de sprites.
        """
        # Define a pasta do herói antes da base se precisarmos de customização
        hero_folder = 'Swordsman' if name == 'Player1' else 'Archer'
        
        # Chama o construtor da Entity passando o frame inicial como imagem base
        # Usamos uma imagem placeholder qualquer, pois os frames sobrescrevem self.surf logo depois
        super().__init__(name, position, img_path=f'./asset/players/{hero_folder}/Walk.png')
        
        self.frame_index = 0
        self.animation_speed = 0.2
        self.state = 'Walk'
        self.facing_left = False
            
        # Carregamento específico de animações
        self.images_walk = self._load_frames(hero_folder, 'Walk', 8)
        self.images_run = self._load_frames(hero_folder, 'Run', 8)
        
        # Garante que a superfície inicial venha da lista de frames carregados
        self.surf = self.images_walk[0]
        self.speed = ENTITY_SPEED[self.name]

    def _load_frames(self, hero_folder, action, num_frames):
        """Fatia a folha de sprites horizontal em frames individuais e escala."""
        sheet = pygame.image.load(f'./asset/players/{hero_folder}/{action}.png').convert_alpha()
        width = sheet.get_width() // num_frames
        height = sheet.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface((i * width, 0, width, height))
            # Escalonamento para visualização ideal na trilha da floresta
            frame = pygame.transform.scale(frame, (100, 100))
            frames.append(frame)
        return frames

    def move(self):
        """Atualiza posição e estado de animação com base no input do teclado."""
        pressed_key = pygame.key.get_pressed()
        
        # Logica de Corrida (Turbo)
        run_key = PLAYER_KEY_RUN[self.name]
        is_running = pressed_key[run_key]
        speed_mult = 2.5 if is_running else 1.0 
        self.state = 'Run' if is_running else 'Walk'
        
        moving = False
        # Movimentação Vertical (Eixo Y limitado à trilha)
        if pressed_key[PLAYER_KEY_UP[self.name]]:
            self.rect.y -= int(self.speed * speed_mult)
            moving = True
        if pressed_key[PLAYER_KEY_DOWN[self.name]]:
            self.rect.y += int(self.speed * speed_mult)
            moving = True
            
        # Movimentação Horizontal
        if pressed_key[PLAYER_KEY_LEFT[self.name]]:
            self.rect.x -= int(self.speed * speed_mult)
            moving = True
            self.facing_left = True
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.x += int(self.speed * speed_mult)
            moving = True
            self.facing_left = False

        # Constrição da área jogável (Restrição de movimento)
        self.rect.top = max(self.rect.top, int(WIN_HEIGHT * 0.18))
        self.rect.bottom = min(self.rect.bottom, int(WIN_HEIGHT * 0.85))
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIN_WIDTH)
            
        # Maquina de Estados de Animação
        if moving:
            self.frame_index += self.animation_speed
            anim_list = self.images_run if self.state == 'Run' else self.images_walk
            if self.frame_index >= len(anim_list):
                self.frame_index = 0
            self.surf = anim_list[int(self.frame_index)]
        else:
            self.frame_index = 0
            self.surf = self.images_run[0] if self.state == 'Run' else self.images_walk[0]
            
        # Inversão de sprite para direção esquerda
        if self.facing_left:
            self.surf = pygame.transform.flip(self.surf, True, False)
