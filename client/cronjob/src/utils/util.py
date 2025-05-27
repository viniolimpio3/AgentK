import os 
from dotenv import load_dotenv
load_dotenv()

def getEnv(key):
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} not set.")
    return value

def build_where_clause(filters):
    """
    Dado um dict {coluna: valor, ...}, retorna:
      - um trecho SQL "WHERE coluna1 = ? AND coluna2 = ? ..." ou "" se vazio
      - a lista de valores [valor1, valor2, ...] para bind
    """
    if not filters:
        return "", []
    clauses = []
    params = []
    for col, val in filters.items():
        clauses.append(f"{col} = ?")
        params.append(val)
    where_sql = "WHERE " + " AND ".join(clauses)
    return where_sql, params
