import os
import json
import requests
import datetime
from src.utils.logger import logger
from src.services.api_k.api_k_requests import analyze
from src.services.db.models import llm_response_history as llm
from src.utils.files import get_k8s_yamls_merged, make_yaml_file, save_corrected_yaml

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    try:     
        # Busca os arquivos YAML mesclando-os em um único arquivo
        logger.info("Listando diretório...")
        file, content = get_k8s_yamls_merged()

        # Envia o arquivo para a API do AgentK realizar a análise
        logger.info("Enviando arquivos para análise...")
        response = analyze(file)

        ai_response = response['result']['choices'][0]['message']['content']
        logger.info(f"Análise realizada com sucesso. Score: {ai_response['score']}. {ai_response['scoreCriteria']}")

        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        corrected_filename = f"correction-{current_datetime}.yaml"

        llm.insert(
            filename = corrected_filename,
            llm_model = response['result']['model'],
            llm_response_json = json.dumps(ai_response),
            yaml_input = content,
            score = ai_response['score'],
            score_criteria = ai_response['scoreCriteria'],
            input_tokens = response['result']['usage']['prompt_tokens'], 
            output_tokens = response['result']['usage']['completion_tokens'],
            llm_response_time_duration = response['response_time']
        )

        save_corrected_yaml(ai_response['correctedFile'], corrected_filename)

        logger.info(f"Arquivo corrigido salvo como {corrected_filename}.")

    except Exception as e:
        print(f"Error: {e} {e.__traceback__}")