import sqlite3
from datetime import datetime
from src.config import DB_PATH

def connect():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute('PRAGMA foreign_keys = ON')
    except sqlite3.Error as e:
        print(f"Error enabling foreign keys: {e}")
        conn.close()
        raise
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS change_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER,
            score_criteria,
            filename TEXT, -- Caminho do arquivo ORIGINAL analisado
            suggested_filename TEXT DEFAULT NULL, -- Caminho do arquivo sugerido pelo LLM
            json_llm_response TEXT,
            timestamp TEXT -- ISO 8601 format (e.g., "2023-03-15T12:34:56")
        )
    ''')
    conn.commit()  # Commit the transaction after executing the CREATE TABLE statement
    conn.close()

def insert_log(nome_arquivo, descricao):
    conn = connect()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()  # Ensure ISO 8601 format
    cursor.execute('INSERT INTO change_logs (timestamp, nome_arquivo, descricao, json_llm_response, score) VALUES (?, ?, ?, ?, ?)',
                   (timestamp, nome_arquivo, descricao, None, None))  # Adjust the last two values as needed
    conn.commit()
    conn.close()
