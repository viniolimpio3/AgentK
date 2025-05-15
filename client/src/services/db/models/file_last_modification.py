from src.services.db.database import connect
from src.utils.util import build_where_clause
from datetime import datetime

def fetch_all():
    """
    Retorna todas as linhas de file_last_modification.
    """
    sql = "SELECT * FROM file_last_modification;"
    with connect() as conn:
        return conn.execute(sql).fetchall()

def fetch_by(filters):
    """
    Retorna linhas de file_last_modification que satisfaçam os filtros.
    Normalmente você vai filtrar por {"filename": "..."}.
    """
    where_sql, params = build_where_clause(filters)
    sql = f"SELECT * FROM file_last_modification {where_sql};"
    with connect() as conn:
        return conn.execute(sql, params).fetchall()
    
def upsert(filename: str, st_mtime: str):
    """
    Insere ou atualiza o registro de última modificação.
    Usa ON CONFLICT para upsert.
    """
    sql = """
    INSERT INTO file_last_modification (filename, st_mtime)
    VALUES (?, ?)
    ON CONFLICT(filename) DO UPDATE SET
      st_mtime=excluded.st_mtime;
    """
    with connect() as conn:
        conn.execute(sql, (filename, st_mtime))
        conn.commit()