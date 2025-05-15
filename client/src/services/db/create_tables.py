from datetime import datetime
from src.utils.util import build_where_clause
from services.db.database import connect

def create_tables():
    """
    Cria as tabelas do MER, se não existirem.
    """
    ddl_history = """
    CREATE TABLE IF NOT EXISTS llm_response_history (
        id                 INTEGER PRIMARY KEY AUTOINCREMENT,
        score              INTEGER,
        score_criteria     TEXT,
        filename           TEXT    NOT NULL,   -- caminho do arquivo original
        created_at         TEXT    NOT NULL,   -- ISO 8601
        llm_model          TEXT,
        llm_response       TEXT,               -- JSON puro
        llm_input_tokens   INTEGER,
        llm_output_tokens  INTEGER,
        llm_time_duration  TEXT                -- ISO 8601 (duração)
    );
    CREATE INDEX IF NOT EXISTS idx_history_filename
        ON llm_response_history(filename);
    """

    ddl_files = """
    CREATE TABLE IF NOT EXISTS file_last_modification (
        filename   TEXT PRIMARY KEY,           -- chave natural
        st_mtime   TEXT    NOT NULL            -- ISO 8601
    );
    """

    with connect() as conn:
        cursor = conn.cursor()
        cursor.executescript(ddl_history + ddl_files)
        conn.commit()

if __name__ == "__main__":
    create_tables()