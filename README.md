# Macro ETL Portfolio

Projeto de ETL desenvolvido em Python com foco em boas práticas de Engenharia de Dados.

## Objetivo

Extrair dados de uma API pública, realizar transformações e disponibilizar os dados para análise.

## Tecnologias Utilizadas

- Python
- Pandas
- Requests
- SQLAlchemy
- PyArrow

## Estrutura do Projeto

```text
macro_etl_portfolio/
│
├── data/
│   ├── posts.csv
│   └── posts_transformed.csv
│
├── notebooks/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
└── requirements.txt
```

## Pipeline ETL

### Extract

Consome dados da API pública:

https://jsonplaceholder.typicode.com/posts

Os dados são convertidos para DataFrame e salvos em CSV.

### Transform

Realiza transformações nos dados:

- Leitura do CSV
- Criação da coluna `title_length`
- Geração do arquivo transformado

### Load

Carrega os dados transformados e exibe:

- Estrutura do dataset
- Estatísticas descritivas
- Resumo dos dados

## Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar extração

```bash
python src/extract.py
```

### Executar transformação

```bash
python src/transform.py
```

### Executar carga

```bash
python src/load.py
```

## Resultados

Arquivos gerados:

```text
data/posts.csv
data/posts_transformed.csv
```

## Próximas Melhorias

- Implementar logging
- Utilizar arquivos .env
- Exportação em formato Parquet
- Integração com banco de dados
- Testes automatizados
- Dockerização do projeto

## Autor

Ires Borges Neves

Projeto desenvolvido para estudo e portfólio em Engenharia de Dados.