import io
import os
from pathlib import Path
import datetime
from utils.util import getEnv

folder = Path(getEnv("AGENTK_FOLDER_ANALYZE"))

def list_k8s_files():
    path = Path(folder)
    k8s_files = []
    # Lê recursivamente todos os arquivos do diretório
    for file in path.rglob("*"): 
        if file.is_file() and file.suffix in ['.yaml', '.yml'] and "correction" not in file.name:
            k8s_files.append({
                "filename": file.name,
                "path": str(file.resolve()),
                "last_modified": datetime.datetime.fromtimestamp(file.stat().st_mtime),
            })
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
    k8s_files = list_k8s_files()
    if len(k8s_files) == 0:
        raise FileNotFoundError(f"No Kubernetes YAML files found in {folder}.")
    
    k8s_yaml_merged = ""
    for file in k8s_files:
        content = get_file_content(file['path'])
        k8s_yaml_merged += content + "\n---\n"

    file = make_yaml_file("k8s_merged.yaml", k8s_yaml_merged)
    return file

def save_corrected_yaml(content):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"correction-{current_datetime}.yaml"
    file = make_yaml_file(filename, content)

    path = Path(folder) / filename
    with open(path, 'wb') as f:
        f.write(file.getbuffer())
    return path.resolve()