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
## Como Rodar com Docker Compose

Além de rodar a aplicação diretamente com o Docker, você também pode usar o `docker-compose` para simplificar a execução, especialmente se você quiser configurar volumes ou executar vários serviços.

### Passos

1. Clone este repositório para a sua máquina (caso ainda não tenha clonado):

    ```bash
    git clone https://github.com/021Antonio/Estudos_Inteli.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd Estudos_Inteli/Provas/Modulo10/prova3
    ```

3. Construa e suba os serviços utilizando o `docker-compose`:

    ```bash
    sudo docker-compose up --build
    ```

    Isso irá construir a imagem do backend e subir a aplicação na porta `8000`.

4. Acesse a documentação interativa da API:

    Após o contêiner ser iniciado com sucesso, abra seu navegador e acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para visualizar a documentação interativa da API, onde você pode testar todos os endpoints.

5. Os logs da aplicação serão salvos no diretório `logs/app.log` do seu projeto, caso precise acessar informações de execução da aplicação.

## Funcionalidades Adicionadas

Além das funcionalidades básicas de criação, atualização, visualização e exclusão de avaliações, os seguintes recursos foram implementados:

- **Sistema de Logging**:
  - Todos os requests e responses da API são registrados, incluindo o método HTTP, a URL requisitada, o código de status da resposta e o tempo de processamento.
  - Os logs são armazenados em um arquivo `logs/app.log` para facilitar a análise e monitoramento da aplicação.
  - Logs também são exibidos no console durante a execução para acompanhamento em tempo real.

- **Estrutura de Middleware para Logs**:
  - Um middleware foi adicionado para capturar informações de cada requisição e resposta, permitindo que o tempo de processamento seja medido e registrado.
  - As informações logadas incluem o método HTTP (GET, POST, PUT, DELETE), o status de resposta (ex: 200, 404) e o tempo total de resposta para cada requisição.

Com essas funcionalidades, a aplicação fica mais robusta e pronta para ser monitorada em ambientes de produção, garantindo que todos os eventos críticos sejam registrados para uma eventual análise.

## Observações sobre a Avaliação

Para a avaliação real deste projeto, **apenas o primeiro commit** é relevante, pois ele foi feito dentro do horário previsto. **Os demais commits foram realizados fora do horário programado**, e servem apenas para ajustes posteriores e conhecimento.
