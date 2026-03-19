#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Item:
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Load a random fruit icon 1-6
        fruit_id = random.randint(1, 6)
        self.surf = pygame.image.load(f'./asset/fruits/{fruit_id}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]

    def move(self, delta_x):
        # Item speed is synced with the "ground" layer (speed 4 in Const.py)
        # We move it based on the scenario scroll
        self.rect.x += delta_x * 4
