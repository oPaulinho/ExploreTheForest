#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Level.py: Orchestrates the life cycle of a game phase. / Orquestra o ciclo de vida de uma fase.
Manages timing, target scores, and active entity sets. / Gerencia tempo, metas e entidades ativas.
"""
import sys
import pygame
from code.Const import (
    DIFFICULTY_SETTINGS, LEVEL_TIMEOUT, LEVEL_TARGET_SCORE, SPAWN_TIME,
    EVENT_SPAWN, EVENT_TIMEOUT, TIMEOUT_STEP, MENU_OPTION, HUD_COLOR_P1,
    HUD_COLOR_P2, C_WHITE, C_YELLOW, WIN_WIDTH, WIN_HEIGHT, C_GREEN
)
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Item import Item
from code.Background import Background
from code.Entity import Entity


class Level:
    """
    Phase manager responsible for victory logic and rendering.
    Gerenciador de fase responsável pela lógica de vitória e renderização.
    """

    def __init__(self, window, name, game_mode, player_score, difficulty):
        """Initializes phase state and difficulty modifiers. / Inicializa estado da fase e modificadores."""
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.difficulty = difficulty
        
        # Difficulty application / Aplicação de dificuldade
        diff_settings = DIFFICULTY_SETTINGS.get(difficulty, DIFFICULTY_SETTINGS['Medium'])
        self.timeout = int(LEVEL_TIMEOUT[self.name] * diff_settings['time_mult'])
        self.target_score = int(LEVEL_TARGET_SCORE[self.name] * diff_settings['goal_mult'])

        self.entity_list = []
        # Factory standardization / Padronização da Factory
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        
        # Phase settings (Morning/Night) / Configurações de fase
        self.message_timer = 3000
        # Instructions only show in Level 1 / Instruções aparecem apenas no Level 1
        self.instruction_timer = 5000 if name == 'Level1' else 0
        if name == 'Level1':
            self.message = "Welcome! Started the Morning. Good luck!"
            self.score_mult = 1
            self.spawn_interval = int(SPAWN_TIME / 2)
        else:
            self.message = "Started the NIGHT! Fruits are worth DOUBLE!"
            self.score_mult = 2
            self.spawn_interval = int(SPAWN_TIME * 1.3)

        # Player inclusion / Inclusão de jogadores
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
        """Main phase loop until victory or timeout. / Loop principal até vitória ou tempo esgotado."""
        song = 'level_1.mp3' if self.name == 'Level1' else 'level_2.mp3'
        pygame.mixer_music.load(f'./asset/{song}')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            # Update and blit cycle / Ciclo de atualização e renderização
            for ent in self.entity_list:
                # Move only after instructions / Move apenas após instruções
                if self.instruction_timer <= 0:
                    # Exclude autonomous movement for Background/Item / Exclui movimento autônomo
                    if not isinstance(ent, (Background, Item)):
                        ent.move()

                self.window.blit(ent.surf, ent.rect)

                # HUD Scoring Interface / Interface de Pontuação
                if self.game_mode == MENU_OPTION[1]:  # Co-op / Cooperativo
                    team_score = sum(e.score for e in self.entity_list if isinstance(e, Player))
                    self.level_text(24, f'TEAM Score: {team_score}', HUD_COLOR_P1, (20, 50))
                else:
                    if ent.name == 'Player1':
                        self.level_text(24, f'P1 Score: {ent.score}', HUD_COLOR_P1, (20, 50))
                    if ent.name == 'Player2':
                        self.level_text(24, f'P2 Score: {ent.score}', HUD_COLOR_P2, (20, 90))

            # HUD Statics / Elementos Fixos do HUD
            self.level_text(20, f'{self.name} - {self.timeout / 1000:.1f}s', C_WHITE, (20, 15))
            self.level_text(20, f'Goal: {self.target_score}', C_YELLOW, (WIN_WIDTH - 150, 15))
            
            if self.message_timer > 0:
                self.level_text(30, self.message, C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2), center=True)

            # Control Instructions Overlay / Overlay de Instruções de Comando
            if self.instruction_timer > 0:
                self.draw_instructions()

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_SPAWN:
                    if len([e for e in self.entity_list if isinstance(e, Item)]) < 30:
                        new_item_list = EntityFactory.get_entity('Item')
                        new_item_list[0].score *= self.score_mult
                        self.entity_list.extend(new_item_list)

                if event.type == EVENT_TIMEOUT:
                    if self.instruction_timer > 0:
                        self.instruction_timer -= TIMEOUT_STEP
                    else:
                        self.timeout -= TIMEOUT_STEP
                        if self.message_timer > 0:
                            self.message_timer -= TIMEOUT_STEP
                        
                    if self.timeout <= 0:
                        # Final scoring verification / Verificação final de pontos
                        p1_score = 0
                        p2_score = 0
                        for ent in self.entity_list:
                            if ent.name == 'Player1':
                                p1_score = ent.score
                            if ent.name == 'Player2':
                                p2_score = ent.score

                        current_score = p1_score + p2_score if self.game_mode == MENU_OPTION[1] else p1_score
                        
                        self.window.fill((0, 0, 0))
                        success = current_score >= self.target_score
                        msg = "CONGRATULATIONS!" if success else "GAME OVER"
                        color = C_GREEN if success else (255, 0, 0)
                        
                        self.level_text(40, msg, color, (WIN_WIDTH / 2, WIN_HEIGHT / 2), center=True)
                        pygame.display.flip()
                        pygame.time.delay(2000)

                        if success:
                            player_score[0] += p1_score
                            player_score[1] += p2_score
                            return True
                        return False

    def level_text(self, text_size: int, text: str, text_color: tuple,
                   text_pos: tuple, center=False):
        """Text rendering helper for fixed or centered alignment. / Auxiliar de renderização de texto."""
        font_name = "Lucida Sans Typewriter"
        font = pygame.font.SysFont(name=font_name, size=text_size, bold=True)
        render_text = font.render(text, True, text_color)
        if center:
            pos = render_text.get_rect(center=text_pos)
            self.window.blit(render_text, pos)
        else:
            self.window.blit(render_text, text_pos)

    def draw_instructions(self):
        """Displays movement controls overlay. / Exibe overlay de controles de movimento."""
        # Simple semi-transparent background for readability / Fundo semi-transparente
        overlay = pygame.Surface((WIN_WIDTH, 120))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.window.blit(overlay, (0, WIN_HEIGHT - 120))

        # Player 1 Instructions
        self.level_text(18, "P1: Walk: ^ v < >", C_WHITE, (50, WIN_HEIGHT - 100))
        self.level_text(18, "P1: Run: R.CTRL + ^ v < >", C_WHITE, (50, WIN_HEIGHT - 70))

        # Player 2 Instructions (if mode requires)
        if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.level_text(18, "P2: Walk: W A S D", C_WHITE, (WIN_WIDTH - 300, WIN_HEIGHT - 100))
            self.level_text(18, "P2: Run: L.CTRL + W A S D", C_WHITE, (WIN_WIDTH - 300, WIN_HEIGHT - 70))

        self.level_text(16, f"Starting in {self.instruction_timer / 1000:.1f}s...", C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT - 30), center=True)