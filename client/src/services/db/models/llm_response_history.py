from src.services.db.database import connect
from src.utils.util import build_where_clause
from datetime import datetime

def fetch_all():
    """
    Retorna todas as linhas de llm_response_history.
    """
    sql = "SELECT * FROM llm_response_history;"
    with connect() as conn:
        return conn.execute(sql).fetchall()

def fetch_by(filters):
    """
    Retorna linhas de llm_response_history que satisfaçam os filtros.
    Exemplo de filtros: {"filename": "foo.txt", "score": 100}
    """
    where_sql, params = build_where_clause(filters)
    sql = f"SELECT * FROM llm_response_history {where_sql};"
    with connect() as conn:
        return conn.execute(sql, params).fetchall()
    
def insert(
    filename: str,
    llm_model: str,
    llm_response_json: str,
    score: int = None,
    score_criteria: str = None,
    input_tokens: int = None,
    output_tokens: int = None
):
    """
    Insere um registro na llm_response_history.
    created_at é gerado aqui, em ISO 8601.
    """
    sql = """
    INSERT INTO llm_response_history (
        filename, created_at, llm_model, llm_response,
        score, score_criteria, llm_input_tokens, llm_output_tokens
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
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
    )
    with connect() as conn:
        conn.execute(sql, params)
        conn.commit()