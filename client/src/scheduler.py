import sched
import time
from src.config import SCHEDULER_INTERVAL

s = sched.scheduler(time.time, time.sleep)
def start_scheduler():
    # Inicializa o scheduler utilizando a função time.time e time.sleep para delay

    # Agenda o primeiro job (executa imediatamente)
    s.enter(0, 1, job)

    # Inicia o loop do scheduler
    s.run()

def job():
    # TODO: adicionar uma requisição http para o servidor

    list_files = ["example.yaml"]  # Exemplo de lista de arquivos YAML a serem analisados

    print("Job executed at", time.ctime())
    s.enter((SCHEDULER_INTERVAL * 60), 1, job)
