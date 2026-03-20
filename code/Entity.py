#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Entity.py: Abstract base class for all game objects. / Classe base abstrata para todos os objetos do jogo.
Provides common structure for asset loading, positioning, and attributes. / Fornece a estrutura comum de carregamento de assets, posicionamento e atributos.
"""
from abc import ABC, abstractmethod
import pygame.image
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    """
    Solid base for any interactive or visual object in the game.
    Base sólida para qualquer objeto interativo ou visual no jogo.
    """

    def __init__(self, name: str, position: tuple, img_path: str = None):
        """
        Initializes central entity attributes. / Inicializa os atributos centrais da entidade.
        """
        self.name = name
        
        # Centralized loading: uses img_path if provided, else default naming convention.
        # Carregamento centralizado: se img_path for fornecido, usa ele; senão usa o padrão por nome.
        final_path = img_path if img_path else f'./asset/{name}.png'
        self.surf = pygame.image.load(final_path).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        
        # Inherited attributes guaranteed in base constructor. / Atributos herdados garantidos no construtor base.
        self.health = ENTITY_HEALTH.get(name, 100)
        self.damage = ENTITY_DAMAGE.get(name, 0)
        self.score = ENTITY_SCORE.get(name, 0)
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        """
        Mandatory contract: defines how the entity moves or updates.
        Contrato obrigatório: define como a entidade se desloca ou atualiza.
        """
        pass
