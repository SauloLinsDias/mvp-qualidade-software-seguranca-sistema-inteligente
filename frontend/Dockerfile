# Frontend Dockerfile
FROM node:20-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do frontend
COPY . /app

# Instala as dependências
RUN npm install

# Compila a aplicação para produção
RUN npm run build

# Usa o nginx para servir os arquivos estáticos
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html

# Copia o arquivo de configuração do nginx (opcional)
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
