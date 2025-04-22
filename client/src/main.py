import requests
import os

from utils.files import get_k8s_yamls_merged, make_yaml_file, save_corrected_yaml
from services.api_k.api_k_requests import analyze

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    try: 
        file = get_k8s_yamls_merged() # Busca os arquivos YAML mesclado em um único arquivo
        response = analyze(file) # Envia o arquivo para a API do AgentK realizar a análise
        print(response['result'])
        print(type(response['result']))
        ai_response = response['result']['choices'][0]['message']['content']
        save_corrected_yaml(ai_response['correctedFile']) # Salva o arquivo corrigido no mesmo diretório dos arquivos originais
    except Exception as e:
        print(f"Error: {e} {e.__traceback__}")