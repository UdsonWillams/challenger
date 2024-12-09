# Careers API

Esta é uma API para gerenciar carreiras, construída com Python 3.12, Django 5.1.3 e PostgreSQL.

## Requisitos

- Python 3.12
- Docker  & Docker Compose

## Configuração

1. Clone o repositório:

   ```sh
   git clone https://github.com/UdsonWillams/challenger
   ```

2. Crie o arquivo `.env` com base no `.env.example`:

   ```sh
   cp .env.example .env
   ```

3. Atualize as variáveis de ambiente no arquivo `.env` conforme necessário.

## Executando a Aplicação

1. Construa e inicie os contêineres Docker:

   ```sh
   docker-compose up --build
   ```

2. Acesse a aplicação em `http://localhost:8000`.

## Endpoints da API

A API possui os seguintes endpoints:

- `GET /careers/` - Lista todas as carreiras
- `POST /careers/` - Cria uma nova carreira
- `PATCH /careers/<int:pk>` - Atualiza uma carreira existente
- `DELETE /careers/<int:pk>` - Deleta uma carreira existente

## Documentação da API

A aplicação possui Swagger para documentação da API. Acesse a documentação em `http://localhost:8000/swagger/`.

## Testes

Para rodar os testes, use o seguinte comando:

```sh
python3 manage.py test
```

## Ferramentas de Desenvolvimento

Esta aplicação utiliza as seguintes ferramentas de desenvolvimento:

- pre-commit para hooks de commit
- Ruff para linting e formatação de código
- ipdb para debugging
