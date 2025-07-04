# Backend - MVP Predição de Doenças Cardíacas

Este é o backend do projeto MVP, desenvolvido com o microframework **Flask**. Ele fornece uma API REST para receber dados de pacientes, realizar predições e armazenar os resultados em um banco de dados.

## 🚀 Instruções para rodar o backend

1. **Crie e ative o ambiente virtual (venv):**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate.bat       # Windows
   ```

2. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute as migrations (SQLAlchemy):**

   ```bash
   flask db upgrade
   ```

4. **Inicie o servidor Flask:**

   ```bash
   flask run
   ```

A aplicação estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 📁 Estrutura

- `app/` - Código-fonte da API
- `app/models.py` - Definição das tabelas do banco
- `app/routes.py` - Rotas da API
- `migrations/` - Histórico das migrações de banco
