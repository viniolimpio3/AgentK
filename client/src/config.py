import os

# Pasta base do agentk
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

# Intervalo de execução do scheduler em minutos
SCHEDULER_INTERVAL = 5

# Caminho do banco de dados SQLite
DB_PATH = 'agentk.db'