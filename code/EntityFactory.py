#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
EntityFactory.py: Padroniza a criação de objetos do jogo. 
Sempre retorna listas de entidades para facilitar a iteração no loop de nível.
"""
import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Item import Item


class EntityFactory:
    """Fábrica estática para instanciar jogadores, itens e fundos."""

    @staticmethod
    def get_entity(entity_name: str) -> list:
        """
        Gera e retorna a entidade solicitada sempre dentro de uma lista.
        
        Args:
            entity_name (str): Nome identificador da entidade.
            
        Returns:
            list: Lista contendo a(s) instância(s) criada(s).
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
                # Cria um item em posição randômica válida
                return [Item(
                    'Item',
                    (random.randint(40, WIN_WIDTH - 40), 
                     random.randint(int(WIN_HEIGHT * 0.25), int(WIN_HEIGHT * 0.82)))
                )]
        return []