# Dockerfile para backend Flask
FROM python:3.13-slim

# Diretório de trabalho
WORKDIR /app

# Instala dependências de sistema necessárias
RUN apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y build-essential libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia os arquivos do backend
COPY . /app/

# Instala as dependências
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


# Expõe a porta padrão do Flask
EXPOSE 5000

# Variável de ambiente para produção
ENV FLASK_APP=app:create_app
ENV FLASK_RUN_HOST=0.0.0.0

RUN chmod +x /app/entrypoint.sh

CMD ["/bin/sh", "/app/entrypoint.sh"]
