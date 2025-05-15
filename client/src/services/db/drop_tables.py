
from src.services.db.database import connect

def drop_tables():
    """
    Remove as tabelas llm_response_history e file_last_modification
    (DROP IF EXISTS para não dar erro caso já não existam).
    """
    ddl = """
    DROP TABLE IF EXISTS llm_response_history;
    DROP TABLE IF EXISTS file_last_modification;
    """
    with connect() as conn:
        conn.executescript(ddl)
        conn.commit()

if __name__ == "__main__":
    drop_tables()