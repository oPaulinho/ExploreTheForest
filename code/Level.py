#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Level.py: Orquestra o ciclo de vida de uma fase.
Gerencia o tempo, metas de pontuação e o conjunto de entidades ativas.
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
    """Gerenciador de fase responsavel pela lógica de vitória e renderização."""

    def __init__(self, window, name, game_mode, player_score, difficulty):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.difficulty = difficulty
        
        # Aplicação de modificadores baseados na dificuldade selecionada
        diff_settings = DIFFICULTY_SETTINGS.get(difficulty, DIFFICULTY_SETTINGS['Medium'])
        self.timeout = int(LEVEL_TIMEOUT[self.name] * diff_settings['time_mult'])
        self.target_score = int(LEVEL_TARGET_SCORE[self.name] * diff_settings['goal_mult'])

        self.entity_list = []
        # Padronização Factory: Agora usamos .extend() universalmente
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        
        # Configurações de fase (Manhã/Noite)
        self.message_timer = 3000 
        if name == 'Level1':
            self.message = "Welcome! Started the Morning. Good luck!"
            self.score_mult = 1
            self.spawn_interval = int(SPAWN_TIME / 2)
        else:
            self.message = "Started the NIGHT! Fruits are worth DOUBLE!"
            self.score_mult = 2
            self.spawn_interval = int(SPAWN_TIME * 1.3)

        # Inclusão de jogadores com reset de score local
        p1_list = EntityFactory.get_entity('Player1')
        p1_list[0].score = 0
        self.entity_list.extend(p1_list)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            p2_list = EntityFactory.get_entity('Player2')
            p2_list[0].score = 0
            self.entity_list.extend(p2_list)

        pygame.time.set_timer(EVENT_SPAWN, self.spawn_interval)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score):
        """Loop de execução da fase até vitória ou término de tempo."""
        song = 'level_1.mp3' if self.name == 'Level1' else 'level_2.mp3'
        pygame.mixer_music.load(f'./asset/{song}')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            # Ciclo de atualização de entidades
            for ent in self.entity_list:
                if not isinstance(ent, (Background, Item)):
                    ent.move() 

                self.window.blit(ent.surf, ent.rect)

                # Interface de Pontuação (HUD)
                if self.game_mode == MENU_OPTION[1]: # Cooperativo
                    team_score = sum(e.score for e in self.entity_list if isinstance(e, Player))
                    self.level_text(24, f'TEAM Score: {team_score}', HUD_COLOR_P1, (20, 50))
                else:
                    if ent.name == 'Player1':
                        self.level_text(24, f'P1 Score: {ent.score}', HUD_COLOR_P1, (20, 50))
                    if ent.name == 'Player2':
                        self.level_text(24, f'P2 Score: {ent.score}', HUD_COLOR_P2, (20, 90))

            # Exibição de Cronômetro e Metas
            self.level_text(20, f'{self.name} - {self.timeout / 1000:.1f}s', C_WHITE, (20, 15))
            self.level_text(20, f'Goal: {self.target_score}', C_YELLOW, (WIN_WIDTH - 150, 15))
            
            if self.message_timer > 0:
                self.level_text(30, self.message, C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2), center=True)

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

                if event.type == EVENT_SPAWN:
                    if len([e for e in self.entity_list if isinstance(e, Item)]) < 30:
                        new_item_list = EntityFactory.get_entity('Item')
                        new_item_list[0].score *= self.score_mult
                        self.entity_list.extend(new_item_list)

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.message_timer > 0:
                        self.message_timer -= TIMEOUT_STEP
                        
                    if self.timeout <= 0:
                        # Verificação final de score vs meta
                        p1_score = 0
                        p2_score = 0
                        for ent in self.entity_list:
                            if ent.name == 'Player1': p1_score = ent.score
                            if ent.name == 'Player2': p2_score = ent.score

                        current_score = p1_score + p2_score if self.game_mode == MENU_OPTION[1] else p1_score
                        
                        self.window.fill((0, 0, 0))
                        success = current_score >= self.target_score
                        msg = ""
                        if success:
                            msg = "CONGRATULATIONS! YOU PASSED!" if self.name == 'Level1' else "VICTORY! YOU SURVIVED!"
                            color = C_GREEN
                        else:
                            msg = "YOU DIED OF HUNGER! GAME OVER"
                            color = (255, 0, 0)
                        
                        self.level_text(40, msg, color, (WIN_WIDTH / 2, WIN_HEIGHT / 2), center=True)
                        pygame.display.flip()
                        pygame.time.delay(2000)

                        if success:
                            player_score[0] += p1_score
                            player_score[1] += p2_score
                            return True
                        return False

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, center=False):
        """Metodo auxiliar de renderização de texto centralizado ou fixo."""
        font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True)
        render_text = font.render(text, True, text_color)
        if center:
            pos = render_text.get_rect(center=text_pos)
            self.window.blit(render_text, pos)
        else:
            self.window.blit(render_text, text_pos)