#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Entity.py: Abstract base class for all game objects (Players, Background layers, Items).
Defines common attributes like name, position, health, and score.
"""
from abc import ABC, abstractmethod
import pygame.image
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    """Base class for every interactive object in the game."""

    def __init__(self, name: str, position: tuple):
        """
        Initializes an entity with basic stats and surface.
        
        Args:
            name (str): Identifier for the entity (matches Const.py keys).
            position (tuple): Initial (x, y) coordinates.
        """
        self.name = name
        # Loads image directly from root asset folder for items that follow this pattern
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        # Base attributes from Const.py
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        """Abstract method to be implemented by children to handle movement logic."""
        pass
