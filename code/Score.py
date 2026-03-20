#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Score.py: Gerencia a exibição e o salvamento dos placares dos jogadores.
"""
import sys
from datetime import datetime
import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.surface import Surface
from pygame.font import Font
from pygame.rect import Rect
from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE, WIN_WIDTH, WIN_HEIGHT
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/background/PNG/game_background_2/game_background_2.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int], win: bool):
        pygame.mixer_music.load('./asset/theme.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        name = ''
        running = True
        
        while running:
            self.window.blit(source=self.surf, dest=self.rect)
            title = 'YOU WIN !!' if win else 'YOU DIED ...'
            self.score_text(48, title, C_YELLOW, SCORE_POS['Title'])

            score = player_score[0]
            text = 'Enter Player 1 name (4 characters):'

            if game_mode == MENU_OPTION[1]: 
                score = (player_score[0] + player_score[1])
                text = 'Enter Team name (4 characters):'

            if game_mode == MENU_OPTION[2]: 
                if player_score[1] > player_score[0]:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'

            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({
                            'name': name.upper(), # Auto-uppercase to look better
                            'score': score,
                            'date': get_formatted_date()
                        })
                        db_proxy.close()
                        self.show()
                        running = False
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(20, name.upper(), C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/theme.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        running = True
        while running:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
            # Improved spacing in Label for better alignment
            self.score_text(20, 'NAME       SCORE           DATE        ', C_YELLOW, SCORE_POS['Label'])

            for i, player_score in enumerate(list_score):
                id_, name, score, date = player_score
                # Fixed string formatting for precise column alignment
                # Using spaces to align with the 'NAME SCORE DATE' header
                formatted_score = f"{name:4s}       {score:05d}       {date}"
                self.score_text(20, formatted_score, C_YELLOW, SCORE_POS[i])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"