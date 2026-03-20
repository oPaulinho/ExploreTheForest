#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Level.py: Manages the core gameplay loop for a specific level/phase.
Handles entity updates, scene transition, scoring validation, and failure conditions.
"""
import sys
import pygame
from code.Const import *
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Item import Item
from code.Background import Background


class Level:
    """Class representing a game level with its own music, goal, and duration."""

    def __init__(self, window, name, game_mode, player_score, difficulty):
        """
        Initializes the level state, difficulty, and initial entities.
        
        Args:
            window (Surface): The main Pygame display surface.
            name (str): 'Level1' (Morning) or 'Level2' (Night).
            game_mode (str): Solo, Co-op, or Competitive.
            player_score (list): References to global player scores for accumulation.
            difficulty (str): Easy, Medium, or Hard.
        """
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.difficulty = difficulty
        
        # Difficulty Modifiers: Adjusts base timeout and target score
        diff_settings = DIFFICULTY_SETTINGS.get(difficulty, DIFFICULTY_SETTINGS['Medium'])
        self.timeout = int(LEVEL_TIMEOUT[self.name] * diff_settings['time_mult'])
        self.target_score = int(LEVEL_TARGET_SCORE[self.name] * diff_settings['goal_mult'])

        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        
        # Level-specific settings (Phase logic)
        self.message_timer = 3000  # Duration of center message in ms
        if name == 'Level1':
            self.message = "Welcome! Started the Morning. Good luck!"
            self.score_mult = 1
            self.spawn_interval = int(SPAWN_TIME / 2) # Frequent items in morning
        else:
            self.message = "Started the NIGHT! Fruits are worth DOUBLE!"
            self.score_mult = 2
            self.spawn_interval = int(SPAWN_TIME * 1.3) # Harder to find items at night

        # Player setup
        player = EntityFactory.get_entity('Player1')
        player.score = 0 # Fresh score for current phase
        self.entity_list.append(player)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = 0
            self.entity_list.append(player)

        # Setup Timers
        pygame.time.set_timer(EVENT_SPAWN, self.spawn_interval)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score):
        """
        Main loop for the level. Returns True if target reached, False otherwise.
        """
        song = 'level_1.mp3' if self.name == 'Level1' else 'level_2.mp3'
        pygame.mixer_music.load(f'./asset/{song}')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            # Update & Blit loop
            for ent in self.entity_list:
                if not isinstance(ent, (Background, Item)):
                    ent.move() # Item/BG movement is handled differently

                self.window.blit(ent.surf, ent.rect)

                # HUD Info (Dynamic Scores)
                if self.game_mode == MENU_OPTION[1]: # Co-op: Unified Team Score
                    team_score = sum(e.score for e in self.entity_list if isinstance(e, Player))
                    self.level_text(24, f'TEAM Score: {team_score}', HUD_COLOR_P1, (20, 50))
                else: # Solo/Competitive: Individual display
                    if ent.name == 'Player1':
                        self.level_text(24, f'P1 Score: {ent.score}', HUD_COLOR_P1, (20, 50))
                    if ent.name == 'Player2':
                        self.level_text(24, f'P2 Score: {ent.score}', HUD_COLOR_P2, (20, 90))

            # Static HUD Elements
            self.level_text(20, f'{self.name} - {self.timeout / 1000:.1f}s', C_WHITE, (20, 15))
            self.level_text(20, f'Goal: {self.target_score}', C_YELLOW, (WIN_WIDTH - 150, 15))
            
            # Start Message Overlay
            if self.message_timer > 0:
                self.level_text(30, self.message, C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2), center=True)

            pygame.display.flip()

            # Process Physics & Stats
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

                if event.type == EVENT_SPAWN:
                    # Spawn fruits periodically if list is not saturated
                    if len([e for e in self.entity_list if isinstance(e, Item)]) < 30:
                        new_item = EntityFactory.get_entity('Item')
                        new_item.score *= self.score_mult # Apply phase multiplier (x1 or x2)
                        self.entity_list.append(new_item)

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.message_timer > 0:
                        self.message_timer -= TIMEOUT_STEP
                        
                    if self.timeout <= 0:
                        # End of level logic
                        p1_score = 0
                        p2_score = 0
                        for ent in self.entity_list:
                            if ent.name == 'Player1': p1_score = ent.score
                            if ent.name == 'Player2': p2_score = ent.score

                        # Goal verification
                        if self.game_mode == MENU_OPTION[1]:
                            current_score = p1_score + p2_score
                        else:
                            current_score = p1_score
                        
                        # Show result message
                        self.window.fill((0, 0, 0))
                        if current_score >= self.target_score:
                            msg = "CONGRATULATIONS! YOU PASSED!" if self.name == 'Level1' else "VICTORY! YOU SURVIVED!"
                            color = C_GREEN
                            success = True
                        else:
                            msg = "YOU DIED OF HUNGER! GAME OVER"
                            color = (255, 0, 0)
                            success = False
                        
                        self.level_text(40, msg, color, (WIN_WIDTH / 2, WIN_HEIGHT / 2), center=True)
                        pygame.display.flip()
                        pygame.time.delay(2000)

                        if success:
                            # Accumulate scores for global ranking
                            player_score[0] += p1_score
                            player_score[1] += p2_score
                            return True
                        return False # Defeat (returns to menu)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, center=False):
        """Helper to render text on the level surface."""
        font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True)
        render_text = font.render(text, True, text_color)
        if center:
            pos = render_text.get_rect(center=text_pos)
            self.window.blit(render_text, pos)
        else:
            self.window.blit(render_text, text_pos)