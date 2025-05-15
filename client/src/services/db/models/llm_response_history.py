from datetime import datetime
from src.services.db.database import connect
from src.utils.util import build_where_clause
from src.utils.logger import logger

def fetch_all():
    try:
        """
        Retorna todas as linhas de llm_response_history.
        """
        sql = "SELECT * FROM llm_response_history;"
        with connect() as conn:
            return conn.execute(sql).fetchall()
    except Exception as e:
        logger.error(f"Erro ao buscar registros no sqlite: {e}")
        raise Exception(f"Erro ao buscar registros no sqlite: {e}")

def fetch_by(filters):
    try:
        """
        Retorna linhas de llm_response_history que satisfaçam os filtros.
        Exemplo de filtros: {"filename": "foo.txt", "score": 100}
        """
        where_sql, params = build_where_clause(filters)
        sql = f"SELECT * FROM llm_response_history {where_sql};"
        with connect() as conn:
            return conn.execute(sql, params).fetchall()
    except Exception as e:
        logger.error(f"Erro ao buscar registros no sqlite: {e}")
        raise Exception(f"Erro ao buscar registros no sqlite: {e}")
    
def insert(
    filename: str,
    llm_model: str,
    llm_response_json: str,
    score: int,
    score_criteria: str,
    input_tokens: int,
    output_tokens: int,
    llm_response_time_duration: int
):
    try:
        """
        Insere um registro na llm_response_history.
        created_at é gerado aqui, em ISO 8601.
        """
        sql = """
        INSERT INTO llm_response_history (
            filename, created_at, llm_model, llm_response,
            score, score_criteria, llm_input_tokens, llm_output_tokens, llm_response_time_duration
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        params = (
            filename,
            datetime.utcnow().isoformat(),
            llm_model,
            llm_response_json,
            score,
            score_criteria,
            input_tokens,
            output_tokens,
            llm_response_time_duration
        )
        with connect() as conn:
            conn.execute(sql, params)
            conn.commit()
    except Exception as e:
        logger.error(f"Erro ao inserir registro: {e}")
        raise Exception(f"Erro ao inserir registro: {e}")