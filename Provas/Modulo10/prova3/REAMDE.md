# Review API

Esta é uma aplicação simples para você registrar suas avaliações de filmes e séries. Com esta API, você pode adicionar o nome do avaliador, o filme ou série que foi assistido, a nota dada e um comentário sobre o que achou. A aplicação permite criar, atualizar, visualizar e excluir avaliações.

## Funcionalidades

- Adicionar uma nova avaliação
- Ver todas as avaliações
- Ver uma avaliação específica
- Atualizar uma avaliação existente
- Excluir uma avaliação

## Tecnologias Utilizadas

A aplicação foi construída utilizando as seguintes tecnologias:

- **[FastAPI](https://fastapi.tiangolo.com/)**: Um framework moderno e rápido para a criação de APIs com Python.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Uma biblioteca SQL poderosa para Python, utilizada para interagir com o banco de dados relacional.

## Como Rodar com Docker

### Pré-requisitos

- [Docker](https://www.docker.com/) instalado na sua máquina.

### Passos

1. Clone este repositório para a sua máquina:

    ```bash
    git clone https://github.com/021Antonio/Estudos_Inteli.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd Estudos_Inteli/Provas/Modulo10/prova3/src
    ```

3. Construa a imagem Docker:

    ```bash
    sudo docker build -t backend-simples .
    ```

4. Execute o contêiner Docker:

    ```bash
    sudo docker run -p 8000:8000 backend-simples
    ```

5. Acesse a documentação interativa da API:

    Abra seu navegador e acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para visualizar a documentação interativa da API, onde você pode testar todos os endpoints.

## Observações sobre a Avaliação

Para a avaliação real deste projeto, **apenas o primeiro commit** é relevante, pois ele foi feito dentro do horário previsto. **Os demais commits foram realizados fora do horário programado**, e servem apenas para ajustes posteriores e conhecimento.
