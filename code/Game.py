#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Game.py: Main engine orchestrator. / O orquestrador central do motor.
Manages global state transitions between menu, play and rankings.
Gerencia transições globais entre menu, gameplay e rankings.
"""
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    """
    Core class initializing Pygame and managing high-level flow.
    Classe núcleo que inicializa o Pygame e gerencia o fluxo de alto nível.
    """

    def __init__(self):
        """Global initialization and window setup. / Inicialização global e setup de janela."""
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Forest Explore')

    def run(self):
        """
        Infinite application loop coordinating game segments.
        Loop infinito coordenando os segmentos do jogo.
        """
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            
            # 1. Start with menu interaction / Inicia com interação de menu
            menu_return, difficulty = menu.run()

            # 2. Main gameplay execution / Execução do gameplay principal
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Local session tracking / Track de sessão local
                win = False
                
                # Execution of Level 1 (Morning) / Execução Nível 1 (Manhã)
                level = Level(self.window, 'Level1', menu_return, player_score, difficulty)
                level_return = level.run(player_score)
                
                # Advance only if Level 1 is cleared / Avança apenas se passar do Nível 1
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score, difficulty)
                    level_return = level.run(player_score)
                    if level_return:
                        win = True  # Full game victory / Vitória total
                
                # 3. Handle results recording / Gravação de resultados
                score.save(menu_return, player_score, win)
                score.show()

            # 4. View Scoreboard directly / Visão direta do Placar
            elif menu_return == MENU_OPTION[3]:
                score.show()
                
            # 5. Safe application termination / Finalização segura
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()
