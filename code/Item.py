#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Item.py: Especialização de Entity para objetos coletáveis (frutas).
Implementa o contrato sem movimento ativo para manter coerência estrutural.
"""
import random
import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Item(Entity):
    """Representa um item coletável que surge de forma randômica."""

    def __init__(self, name: str, position: tuple):
        """Inicializa a fruta selecionando um dos 6 assets disponíveis."""
        fruit_id = random.randint(1, 6)
        # Chama o construtor base passando o caminho da fruta sorteada
        super().__init__(name, position, img_path=f'./asset/fruits/{fruit_id}.png')
        
        # Escalonamento visual para itens
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]

    def move(self, delta_x=0):
        """
        Itens não possuem movimento autônomo.
        O método move é implementado para cumprir o contrato da classe Entity, 
        mas seu deslocamento real é gerenciado em sincronia com o cenário.
        """
        # O deslocamento horizontal relativo ao cenário é aplicado via self.rect.x diretamente se necessário,
        # mas aqui mantemos o contrato limpo.
        if delta_x:
            self.rect.x += delta_x * 4
