
import requests
import os
from src.services.db.models import llm_response_history as llm
from src.utils.util import getEnv
def analyze(file):
    url = os.getenv("APIK_URL") +  "/api/analyze?model=" + getEnv("APIK_MODEL")
    response = requests.post(
        url, 
        files=[('file', (file.name, file, 'application/x-yaml'))],
        timeout=600
    )
    if response.status_code == 200:
        response_json = response.json()
        response_json["response_time"] = int(response.elapsed.total_seconds())
        return response_json
    else:
        raise Exception(f"Erro ao enviar a requisição: {response.status_code} - {response.text}")
