#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
EntityFactory.py: Responsible for instantiating game entities (Players, Items, Backgrounds)
based on their string names. This centralizes object creation.
"""
import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Item import Item


class EntityFactory:
    """Static factory class for entity instantiation."""

    @staticmethod
    def get_entity(entity_name: str):
        """
        Creates and returns an instance of the requested entity.
        
        Args:
            entity_name (str): Name of the entity to create ('Player1', 'Item', etc.)
            
        Returns:
            list or Entity: A list containing the entity (for backgrounds) or the entity instance.
        """
        match entity_name:

            case 'Level1Bg':
                return [Background('Level1Bg', (0, 0))]

            case 'Level2Bg':
                return [Background('Level2Bg', (0, 0))]

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Item':
                # Re-spawns fruits at random heights and screen positions
                return Item(
                    'Item',
                    (random.randint(40, WIN_WIDTH - 40), 
                     random.randint(int(WIN_HEIGHT * 0.25), int(WIN_HEIGHT * 0.82)))
                )