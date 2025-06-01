
import requests
import os
from src.utils.util import getEnv
from src.utils.logger import logger

def analyze(file):
    try:

        url = os.getenv("APIK_URL") +  "/api/analyze?model=" + getEnv("APIK_MODEL")
        response = requests.request("POST", 
            url, 
            headers={}, 
            data={}, 
            files=[('file', (file.name, file, 'application/x-yaml'))], 
            timeout=60000
        )
        if response.status_code == 200:
            response_json = response.json()
            response_json["response_time"] = int(response.elapsed.total_seconds())
            return response_json
        else:
            msg = f"Erro ao enviar a requisição: {response.status_code} - {response.text}"
            logger.error(msg)
            raise Exception(msg)
    except Exception as e:
        msg = f"Erro ao analisar o arquivo: {str(e)}"
        logger.error(msg)
        raise Exception(msg) from e
