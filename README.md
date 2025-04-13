# 🛡️ AgentK

Este projeto é uma API desenvolvida com FastAPI que permite o upload de arquivos YAML (.yaml ou .yml), realizando validações de:

- ✅ Tipo MIME e extensão do arquivo
- ✅ Validação com Large Language Model a estrutura e conteúdo YAML

---

## 📸 AgentK - API

<p align="center">
  <img src="docs/AgentK-color.png" alt="AgentK" width="500" />
</p>

---

## 🚀 Bibliotecas Utilizadas

- Python 3.10
- FastAPI 
- Uvicorn
- PyYAML

---

## 📦 Requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes do Python)

---

## ⚙️ Instalação - API K

```bash
git clone https://github.com/viniolimpio3/AgentK.git
cd AgentK/api

# Instale as dependências
pip install -r requirements.txt


```


## ▶️ Como Executar

```bash

cd api
docker-compose build

docker-compose up -d

Acesse: http://127.0.0.1:8000

Swagger: http://127.0.0.1:8000/docs [ToDO]
```

### Analisar seu YAML:

- Enviar o arquivo como multipart/form-data no campo file.
- Executar o cURL abaixo
```bash
curl -X POST "http://localhost:8000/api/analyze" -F "file=@exemplo.yaml"
```

✅ Retorno Esperado

Se o upload e a validação forem bem-sucedidos, o retorno será semelhante a:

```json
    {
    "status": 200,
    "message": "File analyzed successfully",
    "result": {
        "id": "response ID",
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "logprobs": null,
                "message": {
                    "content": {
                        "issues": [
                        ],
                        "score": 65,
                        "scoreCriteria": "Score calculated starting from 100. Deductions: -30 for Critical issue, -20 for High issue, -10 for each Medium issue (x2), -5 for each Low issue (x2). Additional penalty for security best practices violations."
                    },
                    "refusal": null,
                    "role": "assistant",
                    "annotations": null,
                    "audio": null,
                    "function_call": null,
                    "tool_calls": null
                }
            }
        ],
        "created": 1743957036,
        "model": "deepseek-reasoner",
        "object": "chat.completion",
        "service_tier": null,
        "system_fingerprint": "fp_3d5141a69a_prod0225",
        "usage": {
            "completion_tokens": 1020,
            "prompt_tokens": 1094,
            "total_tokens": 2114,
            "completion_tokens_details": null,
            "prompt_tokens_details": {
                "audio_tokens": null,
                "cached_tokens": 1088
            },
            "prompt_cache_hit_tokens": 1088,
            "prompt_cache_miss_tokens": 6
        }
    }
}
```

## 📸 AgentK - Client
## [TODO]