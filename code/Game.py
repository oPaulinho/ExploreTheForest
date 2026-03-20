#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Game.py: The main engine orquestrator. 
Manages the global state machine transitions between the main menu, 
level execution, and scoreboards.
"""
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    """Root class that initializes Pygame and controls the high-level game flow."""

    def __init__(self):
        """Initializes the window and general Pygame settings."""
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Forest Explore')

    def run(self):
        """
        Infinite application loop. Coordinates transitions between different 
        game segments based on user selection.
        """
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            
            # 1. Main Menu Interaction
            menu_return, difficulty = menu.run()

            # 2. Gameplay Flow (New Game selected)
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Local level scores for current run
                win = False
                
                # Start Phase 1 (Morning)
                level = Level(self.window, 'Level1', menu_return, player_score, difficulty)
                level_return = level.run(player_score)
                
                # Advance to Phase 2 (Night) only if Level1 is passed
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score, difficulty)
                    level_return = level.run(player_score)
                    if level_return:
                        win = True # Both phases cleared
                
                # 3. Post-Game results
                score.save(menu_return, player_score, win)
                score.show()

            # 4. View Scoreboard directly
            elif menu_return == MENU_OPTION[3]:
                score.show()
                
            # 5. Exit Application
            elif menu_return == MENU_OPTION[4]:
                pygame.quit(); quit()
            else:
                pygame.quit(); sys.exit()
