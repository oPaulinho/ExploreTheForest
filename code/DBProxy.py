#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
DBProxy.py: Data access layer for persistent score storage.
Uses SQLite to store and retrieve the Top 10 rankings.
"""
import sqlite3


class DBProxy:
    """Proxy class to handle database connection and queries."""

    def __init__(self, db_name: str):
        """Initializes the database and creates the table if it doesn't exist."""
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def save(self, score_dict: dict):
        """Saves a new score entry to the database."""
        self.connection.execute(
            'INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', 
            score_dict
        )
        self.connection.commit()

    def retrieve_top10(self) -> list:
        """Retrieves and returns the Top 10 players ordered by score."""
        return self.connection.execute(
            'SELECT * FROM dados ORDER BY score DESC LIMIT 10'
        ).fetchall()

    def close(self):
        """Safely closes the database connection."""
        return self.connection.close()