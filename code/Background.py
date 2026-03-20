#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Background.py: Handles the visual layers of the game environment.
Supports both static full-screen backgrounds and dynamic scrolling layers (Parallax style).
"""
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Background:
    """Class representing a background layer with infinite scrolling capability."""

    def __init__(self, name: str, position: tuple):
        """
        Initializes a background layer and determines its image path.
        
        Args:
            name (str): Identifier for the level background (e.g. 'Level1Bg') 
                        or a specific layer (e.g. 'bg1_back_land').
            position (tuple): Starting offset.
        """
        self.name = name
        
        # Determine file path based on level
        if 'Bg' in name:
            bg_num = '4' if 'Level1' in name else '1'
            bg_folder = f'game_background_{bg_num}'
            filepath = f'./asset/background/PNG/{bg_folder}/{bg_folder}.png'
        else:
            # For complex parallax layers (if implemented in future)
            bg_type = name.split('_')[0]
            bg_folder = 'game_background_' + bg_type.replace('bg', '')
            filename = name.replace(bg_type + '_', '') + '.png'
            filepath = f'./asset/background/PNG/{bg_folder}/layers/{filename}'

        # Load and scale to window size
        self.surf = pygame.image.load(filepath).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        # Speed 0 means a fixed static background
        self.speed = ENTITY_SPEED.get(self.name, 0)

    def move(self, delta_x=0):
        """
        Calculates the scrolling offset and handles wrap-around logic 
        for infinite background loop.
        
        Args:
            delta_x (float): Horizontal displacement relative to player movement.
        """
        self.rect.x += delta_x * self.speed
        
        # Dual-image wrapping loop: 
        # When an image leaves the screen completely, it teleports to the other side.
        if delta_x < 0:  # Player moving right
            if self.rect.right <= 0:
                self.rect.left += 2 * WIN_WIDTH
        elif delta_x > 0:  # Player moving left
            if self.rect.left >= WIN_WIDTH:
                self.rect.right -= 2 * WIN_WIDTH