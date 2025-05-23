import sqlite3
from datetime import datetime
from src.config import DB_PATH

PRAGMAS = (
    "PRAGMA journal_mode=WAL;",
    "PRAGMA synchronous=NORMAL;",
    "PRAGMA foreign_keys=ON;",
)

def connect():
    """
    Abre uma conexão e já aplica os PRAGMAs recomendados.
    """
    conn = sqlite3.connect(
        DB_PATH,
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        timeout=30,
    )
    for p in PRAGMAS:
        conn.execute(p)
    # Facilita leitura por nome de coluna:
    conn.row_factory = sqlite3.Row
    return conn