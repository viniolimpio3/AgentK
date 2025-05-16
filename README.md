# 🛡️ AgentK

Este projeto é composto por dois componentes principais:

1. **API**: Desenvolvida com FastAPI que realiza análise de arquivos YAML (.yaml ou .yml)
2. **Client**: CronJob que monitora diretórios e envia arquivos YAML para análise

## Validações Realizadas

- ✅ Tipo MIME e extensão do arquivo
- ✅ Validação com Large Language Model da estrutura e conteúdo YAML
- ✅ Análise de boas práticas nos manifestos Kubernetes
- ✅ Score de qualidade da configuração

---

## 📸 AgentK

<p align="center">
  <img src="docs/AgentK-color.png" alt="AgentK" width="500" />
</p>

---

## 🚀 Bibliotecas Utilizadas

### API
- Python 3.10
- FastAPI 
- Uvicorn
- Python-multipart
- OpenAI

### Client
- Python 3.10
- SQLite3
- Requests
- Python-dotenv

---

## 📦 Requisitos

- Python 3.9 ou superior
- Docker e Docker Compose
- Kubernetes cluster local (para o Client)
- pip (gerenciador de pacotes do Python)

---

## ⚙️ Instalação e Execução

### API K

```bash
# Clone o repositório
git clone https://github.com/viniolimpio3/AgentK.git
cd AgentK/api

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais

# Build e execução com Docker Compose
docker-compose build
docker-compose up -d

# A API estará disponível em:
# http://localhost:8000
# Swagger: http://localhost:8000/docs
```

### Client (CronJob)

```bash
cd AgentK/client

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# Build da imagem Docker
docker build -t agent-k/client:v1 .

# Aplique o CronJob no cluster
kubectl apply -f agentk-cronjob.yaml

# Para reiniciar o CronJob (útil durante desenvolvimento)
./reset-img-build-cronjob.sh
```

## 📝 Uso da API

### Analisar arquivo YAML:

```bash
curl -X POST "http://localhost:8000/api/analyze" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@exemplo.yaml"
```

### ✅ Retorno Esperado

```json
{
    "status": 200,
    "message": "File analyzed successfully",
    "result": {
        "issues": [
            {
                "issue": "Título do problema",
                "severity": "Critical|High|Medium|Low",
                "location": "Localização no arquivo",
                "description": "Descrição detalhada",
                "recommendation": "Sugestão de correção"
            }
        ],
        "score": 85,
        "scoreCriteria": "Critérios de pontuação"
    }
}
```

## 🔄 Client (CronJob)

O client executa as seguintes operações:

1. Monitora diretórios configurados em busca de arquivos YAML
2. Mescla múltiplos arquivos em um único YAML
3. Envia para análise na API
4. Armazena resultados em SQLite
5. Salva arquivos corrigidos

O CronJob é configurado para executar a cada 10 minutos por padrão.