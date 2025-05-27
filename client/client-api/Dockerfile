FROM python:3.13.3-alpine

# Define o diretório de trabalho
WORKDIR /api

# Copia as dependências
COPY ./requirements.txt /api/requirements.txt

# Instala os pacotes
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# Copia todo o código da aplicação
COPY ./ /api/

# Expõe a porta do FastAPI
EXPOSE 3333

# Comando que inicia o FastAPI via Uvicorn
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "3333", "--timeout-keep-alive", "30", "--timeout-graceful-shutdown", "600"]