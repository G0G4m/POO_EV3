import sqlite3 as sql

def conn():
    sql.connect(database = r"DataBase\EcoTech.db")