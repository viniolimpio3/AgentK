FROM python:3.13.3-alpine

# Instalar dependências do sistema necessárias para o sqlite3 funcionar
RUN apk add --no-cache \
    sqlite \
    sqlite-dev \
    gcc \
    musl-dev \
    python3-dev

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

VOLUME ["/app"]

# Instala os pacotes
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Comando padrão ao iniciar o container
CMD ["/app/entrypoint.sh"]