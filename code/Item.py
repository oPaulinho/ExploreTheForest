#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Item.py: Represents the collectible fruits in the game.
Items are spawned randomly and move with the scrolling background.
"""
import random
import pygame
from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Item:
    """Class for collectible fruit entities."""

    def __init__(self, name: str, position: tuple):
        """
        Initializes a fruit item picking one of 6 restored assets randomly.
        
        Args:
            name (str): Should be 'Item'.
            position (tuple): Initial spawn coordinates.
        """
        self.name = name
        # Load a random fruit icon from the restored asset folder
        fruit_id = random.randint(1, 6)
        self.surf = pygame.image.load(f'./asset/fruits/{fruit_id}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        # Load stats from Const.py
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]

    def move(self, delta_x):
        """
        Moves the item horizontally based on scenario movement.
        
        Args:
            delta_x (float): The offset from the background scrolling.
        """
        # Multiplier of 4 ensures it syncs with the "ground" layer speed
        self.rect.x += delta_x * 4
