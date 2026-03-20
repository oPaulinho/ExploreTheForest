#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Player.py: Specific implementation for the playable characters (Warrior and Archer).
Handles input-driven movement, sprite-sheet animation, and screen boundaries.
"""
import pygame
from code.Const import (
    ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_RIGHT, 
    PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, PLAYER_KEY_RUN,
    ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE
)
from code.Entity import Entity


class Player(Entity):
    """Class representing a player-controlled hero."""

    def __init__(self, name: str, position: tuple):
        """
        Initializes player with custom animations and state.
        Note: super().__init__ is skipped to allow custom frame loading from folders.
        """
        self.name = name
        self.frame_index = 0
        self.animation_speed = 0.2
        self.state = 'Walk'
        self.facing_left = False
        
        # Choose folder based on player name (P1 = Swordsman, P2 = Archer)
        hero_folder = 'Swordsman' if self.name == 'Player1' else 'Archer'
            
        # Load animation sheets
        self.images_walk = self._load_frames(hero_folder, 'Walk', 8)
        self.images_run = self._load_frames(hero_folder, 'Run', 8)
        
        # Setup initial surface and rect
        self.surf = self.images_walk[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        # Initialize Entity stats manually
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    def _load_frames(self, hero_folder, action, num_frames):
        """
        Loads a sprite sheet, slices it into individual frames, and scales them.
        
        Args:
            hero_folder (str): 'Swordsman' or 'Archer'.
            action (str): 'Walk' or 'Run'.
            num_frames (int): Number of frames in the horizontal sheet.
        """
        surf = pygame.image.load(f'./asset/players/{hero_folder}/{action}.png').convert_alpha()
        width = surf.get_width() // num_frames
        height = surf.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = surf.subsurface((i * width, 0, width, height))
            # Players are scaled to 100x100 to fit the forest walkable path
            frame = pygame.transform.scale(frame, (100, 100))
            frames.append(frame)
        return frames

    def move(self):
        """
        Reads keyboard input, updates character position, 
        and handles frame animation based on movement state.
        """
        pressed_key = pygame.key.get_pressed()
        
        # Sprint Logic
        run_key = PLAYER_KEY_RUN[self.name]
        is_running = pressed_key[run_key]
        speed_mult = 2.5 if is_running else 1.0 
        self.state = 'Run' if is_running else 'Walk'
        
        moving = False
        # Vertical movement (constrained by forest trail)
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

        # Collision with Screen/Forest path boundaries
        # Y is limited to the trail (18% to 85% of height)
        self.rect.top = max(self.rect.top, int(WIN_HEIGHT * 0.18))
        self.rect.bottom = min(self.rect.bottom, int(WIN_HEIGHT * 0.85))
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIN_WIDTH)
            
        # Animation State Machine
        if moving:
            self.frame_index += self.animation_speed
            anim_list = self.images_run if self.state == 'Run' else self.images_walk
            if self.frame_index >= len(anim_list):
                self.frame_index = 0
            self.surf = anim_list[int(self.frame_index)]
        else:
            self.frame_index = 0
            self.surf = self.images_run[0] if self.state == 'Run' else self.images_walk[0]
            
        # Render flip for facing left
        if self.facing_left:
            self.surf = pygame.transform.flip(self.surf, True, False)
