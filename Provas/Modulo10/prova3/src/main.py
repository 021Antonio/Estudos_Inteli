import logging
from fastapi import FastAPI, Request, Response
from time import time
from db import engine
from models.base import Base
from routes import review
import os
from cache import redis_client
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),  
        logging.StreamHandler()  
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Incluindo as rotas da API
app.include_router(review.router)

# Função para criar as tabelas no banco de dados
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    create_tables()

# Middleware para capturar e cachear respostas
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time()

    logger.info(f"Recebendo requisição {request.method} {request.url}")

    # Cria uma chave única para o cache com base no método e na URL
    cache_key = f"{request.method}_{request.url.path}"

    # Verifica se já existe uma resposta cacheada no Redis
    cached_response = redis_client.get(cache_key)
    if cached_response:
        logger.info(f"Retornando resposta do cache para {request.url}")
        # Retorna a resposta do cache como um JSONResponse
        return JSONResponse(content=cached_response.decode())

    # Processa a requisição e captura a resposta
    response = await call_next(request)

    duration = time() - start_time

    logger.info(f"Enviando resposta status_code={response.status_code} "
                f"para {request.method} {request.url} em {duration:.2f}s")

    # Verifica se a resposta é um JSONResponse e se tem status 200
    if response.status_code == 200:
        # Lê o corpo da resposta e armazena no cache
        body = [section async for section in response.body_iterator]
        response_body = b''.join(body).decode()

        # Re-encapsula o corpo da resposta para continuar a transmissão
        response = JSONResponse(content=response_body)
        
        redis_client.setex(cache_key, 300, response_body)

    return response
