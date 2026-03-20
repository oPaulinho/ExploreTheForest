#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Background.py: Entity specialization for scenario layers. / Especialização de Entity para camadas de cenário.
Handles static or moving positioning of background textures. / Gerencia o posicionamento estático ou móvel dos fundos.
"""
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    """
    Represents a background layer with infinite scrolling capability.
    Representa uma camada de fundo com capacidade de repetição infinita.
    """

    def __init__(self, name: str, position: tuple):
        """Determines image path dynamically based on level naming. / Define o caminho da imagem dinamicamente."""
        if 'Bg' in name:
            bg_num = '4' if 'Level1' in name else '1'
            bg_folder = f'game_background_{bg_num}'
            filepath = f'./asset/background/PNG/{bg_folder}/{bg_folder}.png'
        else:
            bg_type = name.split('_')[0]
            bg_folder = 'game_background_' + bg_type.replace('bg', '')
            filename = name.replace(bg_type + '_', '') + '.png'
            filepath = f'./asset/background/PNG/{bg_folder}/layers/{filename}'

        # Initialize base with resolved path / Inicia a base com o caminho resolvido
        super().__init__(name, position, img_path=filepath)
        
        # Scaling to window size / Redimensiona para preencher a janela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED.get(self.name, 0)

    def move(self, delta_x=0):
        """
        Manages horizontal scrolling and wrap-around loop.
        Gerencia a rolagem horizontal e o efeito de wrap-around (looping).
        """
        self.rect.x += delta_x * self.speed
        
        # Teleport logic to keep background infinite / Lógica de teleporte para fundo infinito
        if delta_x < 0:  # Moving right / Movimento para direita
            if self.rect.right <= 0:
                self.rect.left += 2 * WIN_WIDTH
        elif delta_x > 0:  # Moving left / Movimento para esquerda
            if self.rect.left >= WIN_WIDTH:
                self.rect.right -= 2 * WIN_WIDTH