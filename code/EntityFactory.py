#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
EntityFactory.py: Standardizes object creation. / Padroniza a criação de objetos.
Always returns entity lists to simplify iteration in level loops. / Retorna listas para facilitar a iteração no loop de nível.
"""
import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Item import Item


class EntityFactory:
    """
    Static factory to instantiate players, items, and backgrounds.
    Fábrica estática para instanciar jogadores, itens e fundos.
    """

    @staticmethod
    def get_entity(entity_name: str) -> list:
        """
        Returns requested entity wrapped in a list. / Retorna a entidade solicitada sempre em uma lista.
        """
        match entity_name:

            case 'Level1Bg':
                return [Background('Level1Bg', (0, 0))]

            case 'Level2Bg':
                return [Background('Level2Bg', (0, 0))]

            case 'Player1':
                return [Player('Player1', (10, WIN_HEIGHT / 2 - 30))]

            case 'Player2':
                return [Player('Player2', (10, WIN_HEIGHT / 2 + 30))]

            case 'Item':
                # Spawn item at valid random position / Spawn em posição randômica válida
                return [Item(
                    'Item',
                    (random.randint(40, WIN_WIDTH - 40), 
                     random.randint(int(WIN_HEIGHT * 0.25), int(WIN_HEIGHT * 0.82)))
                )]
        return []