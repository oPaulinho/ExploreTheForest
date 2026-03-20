#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
main.py: App entry point. / Ponto de entrada do aplicativo.
Bootstraps the Game engine. / Inicia o motor do jogo.
"""
from code.Game import Game

# Application bootstrap / Partida do aplicativo
if __name__ == '__main__':
    game = Game()
    game.run()
