#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Entity.py: Classe base abstrata para todos os objetos do jogo.
Fornece a estrutura comum de carregamento de assets, posicionamento e atributos.
"""
from abc import ABC, abstractmethod
import pygame.image
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    """Base sólida para qualquer objeto interativo ou visual no jogo."""

    def __init__(self, name: str, position: tuple, img_path: str = None):
        """
        Inicializa os atributos centrais da entidade.
        
        Args:
            name (str): Nome identificador para buscar estatísticas no Const.py.
            position (tuple): Coordenadas iniciais (x, y).
            img_path (str, optional): Caminho customizado da imagem. Se nulo, usa o padrão ./asset/{name}.png.
        """
        self.name = name
        
        # Carregamento centralizado: se img_path for fornecido, usa ele; senão usa o padrão por nome.
        final_path = img_path if img_path else f'./asset/{name}.png'
        self.surf = pygame.image.load(final_path).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        # Atributos herdados garantidos no construtor base
        self.health = ENTITY_HEALTH.get(name, 100)
        self.damage = ENTITY_DAMAGE.get(name, 0)
        self.score = ENTITY_SCORE.get(name, 0)
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        """Contrato obrigatório: define como a entidade se desloca ou atualiza."""
        pass
