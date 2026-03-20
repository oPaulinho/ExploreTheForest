#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Item.py: Entity specialization for collectible fruits. / Especialização de Entity para frutas coletáveis.
Implements movement contract even as a passive object. / Implementa o contrato de movimento mesmo sendo passivo.
"""
import random
import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Item(Entity):
    """
    Represents a score item that spawns randomly.
    Representa um item de pontuação que surge aleatoriamente.
    """

    def __init__(self, name: str, position: tuple):
        """Randomly picks a fruit and sets its physical properties. / Sorteia uma fruta e inicializa suas propriedades."""
        fruit_id = random.randint(1, 6)
        super().__init__(name, position, img_path=f'./asset/fruits/{fruit_id}.png')
        
        # Consistent scaling / Redimensiona para escala uniforme
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        # Update rect size after scaling / Atualiza o rect após redimensionar
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]

    def move(self, delta_x=0):
        """
        Items are shifted in sync with background movement.
        O item é deslocado em sincronia com o movimento do cenário.
        """
        if delta_x:
            self.rect.x += delta_x * 4
