#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Player.py: Implementação dos heróis jogáveis.
Herda de Entity e implementa lógica de animação e entrada do usuário.
"""
import pygame
from code.Const import (
    ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_RIGHT, 
    PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, PLAYER_KEY_RUN
)
from code.Entity import Entity


class Player(Entity):
    """Entidade controlada pelo jogador com suporte a spritesheets e estados."""

    def __init__(self, name: str, position: tuple):
        """Inicializa o jogador e calibra o bounding box (rect) para o tamanho do frame."""
        hero_folder = 'Swordsman' if name == 'Player1' else 'Archer'
        
        # Chamada base para garantir atributos fundamentais
        super().__init__(name, position, img_path=f'./asset/players/{hero_folder}/Walk.png')
        
        self.frame_index = 0
        self.animation_speed = 0.2
        self.state = 'Walk'
        self.facing_left = False
            
        # Carregamento de frames individuais do spritesheet
        self.images_walk = self._load_frames(hero_folder, 'Walk', 8)
        self.images_run = self._load_frames(hero_folder, 'Run', 8)
        
        # AJUSTE CRÍTICO: Atualiza a superfície e o RECT para as dimensões de um frame (100x100)
        # Sem isso, o rect herda o tamanho da folha inteira, causando bugs de movimento e colisão.
        self.surf = self.images_walk[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        self.speed = ENTITY_SPEED[self.name]

    def _load_frames(self, hero_folder, action, num_frames):
        """Divide a folha de sprites em frames e escala para 100x100."""
        sheet = pygame.image.load(f'./asset/players/{hero_folder}/{action}.png').convert_alpha()
        width = sheet.get_width() // num_frames
        height = sheet.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface((i * width, 0, width, height))
            frame = pygame.transform.scale(frame, (100, 100))
            frames.append(frame)
        return frames

    def move(self):
        """Gerencia movimento por teclado e atualiza a animação visual."""
        pressed_key = pygame.key.get_pressed()
        
        # Corrida (Sprinting)
        run_key = PLAYER_KEY_RUN[self.name]
        is_running = pressed_key[run_key]
        speed_mult = 2.5 if is_running else 1.0 
        self.state = 'Run' if is_running else 'Walk'
        
        moving = False
        # Navegação Vertical (Trava na trilha)
        if pressed_key[PLAYER_KEY_UP[self.name]]:
            self.rect.y -= int(self.speed * speed_mult)
            moving = True
        if pressed_key[PLAYER_KEY_DOWN[self.name]]:
            self.rect.y += int(self.speed * speed_mult)
            moving = True
            
        # Navegação Horizontal
        if pressed_key[PLAYER_KEY_LEFT[self.name]]:
            self.rect.x -= int(self.speed * speed_mult)
            moving = True
            self.facing_left = True
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.x += int(self.speed * speed_mult)
            moving = True
            self.facing_left = False

        # Restrições de borda de tela
        self.rect.top = max(self.rect.top, int(WIN_HEIGHT * 0.18))
        self.rect.bottom = min(self.rect.bottom, int(WIN_HEIGHT * 0.85))
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIN_WIDTH)
            
        # Atualização de Frames
        if moving:
            self.frame_index += self.animation_speed
            anim_list = self.images_run if self.state == 'Run' else self.images_walk
            if self.frame_index >= len(anim_list):
                self.frame_index = 0
            self.surf = anim_list[int(self.frame_index)]
        else:
            self.frame_index = 0
            self.surf = self.images_run[0] if self.state == 'Run' else self.images_walk[0]
            
        # Orientação do Sprite
        if self.facing_left:
            self.surf = pygame.transform.flip(self.surf, True, False)
