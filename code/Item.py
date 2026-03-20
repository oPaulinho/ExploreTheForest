#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Item.py: Especialização de Entity para frutas coletáveis.
Implementa o contrato de movimento mesmo sendo um objeto passivo.
"""
import random
import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Item(Entity):
    """Representa um item de pontuação que surge aleatoriamente."""

    def __init__(self, name: str, position: tuple):
        """Sorteia uma fruta e inicializa suas propriedades físicas."""
        fruit_id = random.randint(1, 6)
        super().__init__(name, position, img_path=f'./asset/fruits/{fruit_id}.png')
        
        # Redimensiona para escala uniforme
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        # AJUSTE: Atualiza o rect para o novo tamanho escalado
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]

    def move(self, delta_x=0):
        """O item é deslocado em sincronia com o movimento do cenário."""
        if delta_x:
            self.rect.x += delta_x * 4
