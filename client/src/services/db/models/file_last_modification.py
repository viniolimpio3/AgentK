from src.services.db.database import connect
from src.utils.util import build_where_clause
from src.utils.logger import logger
from datetime import datetime

def fetch_all():
    try: 
        """
        Retorna todas as linhas de file_last_modification.
        """
        sql = "SELECT * FROM file_last_modification;"
        with connect() as conn:
            return conn.execute(sql).fetchall()
    except Exception as e:
        logger.error(f"Erro ao buscar registros no sqlite: {e}")
        raise Exception(f"Erro ao buscar registros no sqlite: {e}")

def fetch_by(filters):
    try:
        """
        Retorna linhas de file_last_modification que satisfaçam os filtros.
        Normalmente você vai filtrar por {"filename": "..."}.
        """
        where_sql, params = build_where_clause(filters)
        sql = f"SELECT * FROM file_last_modification {where_sql};"
        with connect() as conn:
            return conn.execute(sql, params).fetchall()
    except Exception as e:
        logger.error(f"Erro ao buscar registros no sqlite: {e}")
        raise Exception(f"Erro ao buscar registros no sqlite: {e}")
    
def upsert(filename: str, st_mtime: str):
    try:
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
    except Exception as e:
        logger.error(f"Erro ao realizar upsert no sqlite: {e}")
        raise Exception(f"Erro ao realizar upsert no sqlite: {e}")