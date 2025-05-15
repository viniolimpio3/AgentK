import io
import os
from pathlib import Path
import datetime
from src.utils.util import getEnv
from src.utils.logger import logger
from src.services.db.models import file_last_modification as flm

folder = Path(getEnv("AGENTK_FOLDER_ANALYZE"))

def list_k8s_files():
    path = Path(folder)
    k8s_files = []
    # Lê recursivamente todos os arquivos do diretório
    for file in path.rglob("*"): 
        if file.is_file() and file.suffix in ['.yaml', '.yml'] and "correction" not in file.name:
            result = flm.fetch_by({ "filename": file.name })
            if(len(result) == 0 or (len(result) > 0 and result[0]['st_mtime'] != str(datetime.datetime.fromtimestamp(file.stat().st_mtime)))):
                k8s_files.append({
                    "filename": file.name,
                    "path": str(file.resolve()),
                    "last_modified": datetime.datetime.fromtimestamp(file.stat().st_mtime)
                })
                flm.upsert(file.name, str(datetime.datetime.fromtimestamp(file.stat().st_mtime)))

    return k8s_files

def get_file_content(_path):
    path = Path(_path)
    if path.is_file():
        with open(path, 'r', encoding="utf-8") as file:
            return file.read()  
    else:
        raise FileNotFoundError(f"File {path} not found.")
    
def make_yaml_file(filename, content):
    file = io.BytesIO(content.encode('utf-8'))
    file.name = filename
    return file

def get_k8s_yamls_merged():
    try:

        k8s_files = list_k8s_files()

        if len(k8s_files) == 0:
            raise FileNotFoundError(
                f"Arquivos YAML não encontrados, ou não modificados em {folder}."
            )
        
        logger.info(f"Foram encontrados {len(k8s_files)} arquivos YAML modificados.")
        logger.info(f"Lista de arquivos: {str(k8s_files)}")
        
        k8s_yaml_merged = ""
        for file in k8s_files:
            content = get_file_content(file['path'])
            k8s_yaml_merged += content + "\n---\n# File: "+ file['filename'] + "\n"

        file = make_yaml_file("k8s_merged.yaml", k8s_yaml_merged)
        logger.info(f"Arquivo mesclado criado com sucesso. Conteúdo: {k8s_yaml_merged}")

        return file
    except FileNotFoundError as e:
        logger.info(e)
    except Exception as e:
        logger.error(f"Erro ao mesclar arquivos YAML: {e}")
        raise Exception(f"Erro ao mesclar arquivos YAML: {e}")
    
def save_corrected_yaml(content, filename):
    file = make_yaml_file(filename, content)
    path = Path(folder) / filename
    with open(path, 'wb') as f:
        f.write(file.getbuffer())
    return path.resolve()