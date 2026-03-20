#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
EntityMediator.py: Handles the interaction logic between different entities,
primarily focusing on collision detection and score updates.
"""
from code.Player import Player
from code.Item import Item


class EntityMediator:
    """Mediator class that manages interactions between entities."""

    @staticmethod
    def __verify_collision_window(ent):
        """Checks if an entity (like a fruit) has left the screen on the left side."""
        if isinstance(ent, Item) and ent.rect.right < 0:
            ent.health = 0 # Mark for removal

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        """Checks and handles collision between two specific entities."""
        if ent1.rect.colliderect(ent2.rect):

            # Player collecting an Item (Fruit)
            if isinstance(ent1, Player) and isinstance(ent2, Item):
                ent1.score += ent2.score
                ent2.health = 0 # Mark for removal

            # Reversed check for robustness
            elif isinstance(ent1, Item) and isinstance(ent2, Player):
                ent2.score += ent1.score
                ent1.health = 0

    @staticmethod
    def verify_collision(entity_list):
        """Performs global collision checks for all entities in the current level."""
        for i in range(len(entity_list)):
            EntityMediator.__verify_collision_window(entity_list[i])
            for j in range(i + 1, len(entity_list)):
                EntityMediator.__verify_collision_entity(
                    entity_list[i], entity_list[j]
                )

    @staticmethod
    def verify_health(entity_list):
        """Removes entities from the list if their health reaches zero (e.g., after a collision)."""
        for ent in entity_list[:]:
            if isinstance(ent, (Player, Item)):
                if ent.health <= 0:
                    entity_list.remove(ent)