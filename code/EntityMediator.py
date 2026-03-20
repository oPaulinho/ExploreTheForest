#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
EntityMediator.py: Centraliza a gestão de interações físicas e lógica de 
vitalidade entre os componentes do jogo.
"""
from code.Player import Player
from code.Item import Item


class EntityMediator:
    """Classe responsável por mediar eventos entre diferentes entidades de jogo."""

    @staticmethod
    def verify_collision(entity_list: list):
        """Detecta colisões entre jogadores e itens coletáveis."""
        # Itera pelo par de entidades para verificar intersecção de retângulos
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]
                
                # Verificação centralizada de colisão por rect
                if ent1.rect.colliderect(ent2.rect):
                    # Lógica de coleta de itens (Frutas)
                    if isinstance(ent1, Player) and isinstance(ent2, Item):
                        ent1.score += ent2.score
                        ent2.health = 0 # Sinaliza remoção por vitalidade
                    elif isinstance(ent1, Item) and isinstance(ent2, Player):
                        ent2.score += ent1.score
                        ent1.health = 0

    @staticmethod
    def verify_health(entity_list: list):
        """
        Garante a remoção segura de entidades mortas ou coletadas.
        Itera sobre uma cópia da lista [:] para evitar erros de remoção em tempo real.
        """
        for ent in entity_list[:]:
            if isinstance(ent, (Player, Item)):
                if ent.health <= 0:
                    entity_list.remove(ent)