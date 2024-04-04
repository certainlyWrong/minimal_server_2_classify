O repositório contém uma pequena API para executar testes com modelos de Machine Learning. A API foi desenvolvida utilizando o framework FastAPI e o TensorFlow para a execução dos modelos.

## Executando a API

Para executar a API, é necessário ter o [Poetrt](https://python-poetry.org/) instalado. Com o Poetry instalado, execute o comando abaixo para instalar as dependências do projeto:

```bash
poetry install
```

Após a instalação das dependências, execute o comando abaixo para iniciar a API:

```bash
poetry run server
```

Existem também um segundo comando para executar uma requisicao para a API:

```bash
poetry run client <image_path> <server_url>
```
