#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, \
    PLAYER_KEY_UP, PLAYER_KEY_RUN
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        # We don't call super() here because Entity's __init__ loads the specific '.png'
        # Instead we initialize our own variables.
        self.name = name
        self.frame_index = 0
        self.animation_speed = 0.2
        self.state = 'Walk'
        self.facing_left = False
        hero_folder = 'Swordsman' if self.name == 'Player1' else 'Archer'
            
        self.images_walk = self._load_frames(hero_folder, 'Walk', 8)
        self.images_run = self._load_frames(hero_folder, 'Run', 8)
        
        self.surf = self.images_walk[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        # Entity stats
        from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    def _load_frames(self, hero_folder, action, num_frames):
        """Loads and extracts animation frames from a sprite sheet."""
        surf = pygame.image.load(f'./asset/players/{hero_folder}/{action}.png').convert_alpha()
        width = surf.get_width() // num_frames
        height = surf.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = surf.subsurface((i * width, 0, width, height))
            # Scale down the player so it fits the trail (scaled relative to 720p height)
            frame = pygame.transform.scale(frame, (100, 100))
            frames.append(frame)
        return frames

    def move(self):
        """Handles player movement and animation."""
        pressed_key = pygame.key.get_pressed()
        
        # Check sprint and choose state
        run_key = PLAYER_KEY_RUN[self.name]
        is_running = pressed_key[run_key]
        speed_mult = 2.5 if is_running else 1.0 # Boost speed a bit
        self.state = 'Run' if is_running else 'Walk'
        
        moving = False
        # Vertical movement
        if pressed_key[PLAYER_KEY_UP[self.name]]:
            self.rect.y -= int(self.speed * speed_mult)
            moving = True
        if pressed_key[PLAYER_KEY_DOWN[self.name]]:
            self.rect.y += int(self.speed * speed_mult)
            moving = True
        # Horizontal movement
        if pressed_key[PLAYER_KEY_LEFT[self.name]]:
            self.rect.x -= int(self.speed * speed_mult)
            moving = True
            self.facing_left = True
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.x += int(self.speed * speed_mult)
            moving = True
            self.facing_left = False

        # Limits to the walkable forest path and screen bounds
        self.rect.top = max(self.rect.top, int(WIN_HEIGHT * 0.18))
        self.rect.bottom = min(self.rect.bottom, int(WIN_HEIGHT * 0.85))
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIN_WIDTH)
            
        # Animation logic
        if moving:
            self.frame_index += self.animation_speed
            anim_list = self.images_run if self.state == 'Run' else self.images_walk
            if self.frame_index >= len(anim_list):
                self.frame_index = 0
            self.surf = anim_list[int(self.frame_index)]
        else:
            self.frame_index = 0
            self.surf = self.images_run[0] if self.state == 'Run' else self.images_walk[0]
            
        if self.facing_left:
            self.surf = pygame.transform.flip(self.surf, True, False)
