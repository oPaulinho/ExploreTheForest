#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
EntityMediator.py: Central management of physical interactions and vitality logic.
Gerencia as interações físicas e a vitalidade entre os componentes do jogo.
"""
from code.Player import Player
from code.Item import Item


class EntityMediator:
    """
    Mediates events between different game entities.
    Responsável por mediar eventos entre diferentes entidades de jogo.
    """

    @staticmethod
    def verify_collision(entity_list: list):
        """Detects collisions between players and collectible items. / Detecta colisões entre jogadores e itens."""
        # Check pairs for rectangle intersection / Verifica intersecção de retângulos em pares
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]
                
                # Centralized collision check / Verificação centralizada de colisão
                if ent1.rect.colliderect(ent2.rect):
                    # Item collection logic (Fruits) / Lógica de coleta (Frutas)
                    if isinstance(ent1, Player) and isinstance(ent2, Item):
                        ent1.score += ent2.score
                        ent2.health = 0 # Signal for removal / Sinaliza remoção
                    elif isinstance(ent1, Item) and isinstance(ent2, Player):
                        ent2.score += ent1.score
                        ent1.health = 0

    @staticmethod
    def verify_health(entity_list: list):
        """
        Ensures safe removal of dead or collected entities using list slicing.
        Garante a remoção segura de entidades mortas usando cópias de lista [:].
        """
        for ent in entity_list[:]:
            if isinstance(ent, (Player, Item)):
                if ent.health <= 0:
                    entity_list.remove(ent)