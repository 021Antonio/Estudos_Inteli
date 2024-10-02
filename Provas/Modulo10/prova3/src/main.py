import logging
from fastapi import FastAPI, Request
from time import time
from db import engine
from models.base import Base
from routes import review
import os

# Verifica se o diretório de logs existe, se não, cria
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),  # Logs serão salvos no diretório "logs"
        logging.StreamHandler()  # Exibe logs no console
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Incluindo as rotas da API
app.include_router(review.router)

# Função para criar as tabelas no banco de dados
def create_tables():
    Base.metadata.create_all(bind=engine)

# Chama a criação das tabelas no startup
@app.on_event("startup")
async def startup_event():
    create_tables()

# Middleware para logar requisições e respostas
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time()

    # Log da requisição recebida
    logger.info(f"Recebendo requisição {request.method} {request.url}")

    # Processa a requisição
    response = await call_next(request)

    # Calcula o tempo de execução
    duration = time() - start_time

    # Log da resposta
    logger.info(f"Enviando resposta status_code={response.status_code} "
                f"para {request.method} {request.url} em {duration:.2f}s")

    return response
