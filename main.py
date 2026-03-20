#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
main.py: Entry point for the Forest Explore game.
"""
from code.Game import Game

# Bootstrapping
if __name__ == '__main__':
    game = Game()
    game.run()
