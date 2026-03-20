#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
DBProxy.py: SQLite abstraction layer for persistent results.
Camada de abstração SQLite para persistência de resultados.
"""
import sqlite3


class DBProxy:
    """
    Handles local database connection and basic CRUD for scores.
    Gerencia conexão local e CRUD básico para pontuações.
    """

    def __init__(self, db_name: str):
        """Initializes database and table schema. / Inicializa banco e esquema de tabela."""
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
        """Inserts a new entry into the ledger. / Insere nova entrada no registro."""
        self.connection.execute(
            'INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', 
            score_dict
        )
        self.connection.commit()

    def retrieve_top10(self) -> list:
        """Fetch winners ordered by highest score. / Busca vencedores por maior pontuação."""
        return self.connection.execute(
            'SELECT * FROM dados ORDER BY score DESC LIMIT 10'
        ).fetchall()

    def close(self):
        """Safely disconnects from the file. / Desconexão segura do arquivo."""
        return self.connection.close()