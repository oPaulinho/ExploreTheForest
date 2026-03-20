#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Menu.py: Handles the initial screen and user interaction for game mode 
and difficulty selection.
"""
import pygame.image
import sys
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, DIFFICULTY_LEVELS


class Menu:
    """Class representing the main menu system."""

    def __init__(self, window):
        """
        Initializes the menu with background and window reference.
        """
        self.window = window
        self.surf = pygame.image.load('./asset/background/PNG/game_background_3/game_background_3.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        """
        Main loop for the menu. Returns (selected_mode, selected_difficulty).
        """
        menu_option = 0
        pygame.mixer_music.load('./asset/theme.mp3')
        pygame.mixer_music.play(-1)
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Forest", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Explore", C_ORANGE, ((WIN_WIDTH / 2), 120))

            # Render options
            for i in range(len(MENU_OPTION)):
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(20, MENU_OPTION[i], color, ((WIN_WIDTH / 2), 200 + 25 * i))
                
            pygame.display.flip()

            # Handle Menu Navigation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                         menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                         menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        selected_mode = MENU_OPTION[menu_option]
                        
                        # Trigger difficulty selection for play options
                        if selected_mode in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                            return selected_mode, self.select_difficulty()
                        return selected_mode, None

    def select_difficulty(self):
        """
        Sub-menu for choosing Easy, Medium, or Hard.
        Returns the string name of the difficulty.
        """
        diff_option = 1 # Default to Medium
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(40, "Select Difficulty", C_ORANGE, (WIN_WIDTH / 2, 70))
            
            for i in range(len(DIFFICULTY_LEVELS)):
                color = C_YELLOW if i == diff_option else C_WHITE
                self.menu_text(25, DIFFICULTY_LEVELS[i], color, (WIN_WIDTH / 2, 200 + 35 * i))
                
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        diff_option = (diff_option + 1) % len(DIFFICULTY_LEVELS)
                    if event.key == pygame.K_UP:
                        diff_option = (diff_option - 1) % len(DIFFICULTY_LEVELS)
                    if event.key == pygame.K_RETURN:
                        return DIFFICULTY_LEVELS[diff_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Helper for center-aligned text rendering."""
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)