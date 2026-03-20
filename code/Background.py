#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Background.py: Especialização de Entity para camadas de cenário.
Gerencia o posicionamento estático ou móvel das texturas de fundo.
"""
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    """Representa uma camada de fundo com capacidade de repetição infinita."""

    def __init__(self, name: str, position: tuple):
        """
        Inicializa a camada de fundo determinando o caminho da imagem dinamicamente.
        """
        # Lógica de seleção de pasta baseada no nome
        if 'Bg' in name:
            bg_num = '4' if 'Level1' in name else '1'
            bg_folder = f'game_background_{bg_num}'
            filepath = f'./asset/background/PNG/{bg_folder}/{bg_folder}.png'
        else:
            bg_type = name.split('_')[0]
            bg_folder = 'game_background_' + bg_type.replace('bg', '')
            filename = name.replace(bg_type + '_', '') + '.png'
            filepath = f'./asset/background/PNG/{bg_folder}/layers/{filename}'

        # Chama o construtor base com o caminho resolvido
        super().__init__(name, position, img_path=filepath)
        
        # Redimensiona para preencher a janela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED.get(self.name, 0)

    def move(self, delta_x=0):
        """
        Gerencia a rolagem horizontal e o efeito de wrap-around (looping).
        """
        self.rect.x += delta_x * self.speed
        
        # Lógica de teletransporte para manter o fundo infinito
        if delta_x < 0:  # Movimento para a direita
            if self.rect.right <= 0:
                self.rect.left += 2 * WIN_WIDTH
        elif delta_x > 0:  # Movimento para a esquerda
            if self.rect.left >= WIN_WIDTH:
                self.rect.right -= 2 * WIN_WIDTH