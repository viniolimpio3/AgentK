
import requests
import os

def analyze(file):
    
    url = os.getenv("APIK_URL") +  "/api/analyze"
    response = requests.post(url, files=[('file', (file.name, file, 'application/x-yaml'))])
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao enviar a requisição para : {response.status_code} - {response.text}")
