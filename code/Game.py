#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Forest Explore')

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return, difficulty = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                win = False
                level = Level(self.window, 'Level1', menu_return, player_score, difficulty)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score, difficulty)
                    level_return = level.run(player_score)
                    if level_return:
                        win = True
                
                # Save and show score with win/loss status
                score.save(menu_return, player_score, win)
                score.show()

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
