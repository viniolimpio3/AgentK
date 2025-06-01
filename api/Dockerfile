# FROM python:3.13.3-alpine

# # Define o diretório de trabalho
# WORKDIR /api

# # Copia as dependências
# COPY ./requirements.txt /api/requirements.txt

# # Instala os pacotes
# RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# # Copia todo o código da aplicação
# COPY ./ /api/

# # Expõe a porta do FastAPI
# EXPOSE 8000

# # Comando que inicia o FastAPI via Uvicorn
# CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "600", "--timeout-graceful-shutdown", "600"]

FROM python:3.13.3-alpine

# Define o diretório de trabalho
WORKDIR /api

# Copia as dependências
COPY ./requirements.txt /api/requirements.txt

# Instala dependências de sistema (necessárias para gunicorn e dependências C)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Instala os pacotes Python
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# Copia o código da aplicação
COPY ./ /api/

# Expõe a porta da API
EXPOSE 8000

# Comando de produção com Gunicorn + UvicornWorker
CMD ["gunicorn", "run:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--timeout", "600"]
