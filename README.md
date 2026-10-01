# Macro ETL Portfolio

https://github.com/IresBorges/macro_etl_portfolio/actions/workflows/ci.yml/badge.svg](https://github.com/IresBorges/macro_etl_portfolio/actions/workflows/ci.yml)

Projeto profissional de Engenharia de Dados desenvolvido em Python com foco em arquitetura ETL, testes automatizados e integração contínua.

---

## Objetivo

Construir uma pipeline ETL completa capaz de:

- Extrair indicadores macroeconómicos da API FRED
- Transformar os dados com Pandas
- Gerar relatórios profissionais em Excel
- Validar automaticamente a qualidade do código através de testes automatizados
- Executar CI/CD com GitHub Actions

---

## Fonte de Dados

**FRED (Federal Reserve Economic Data)**

Indicadores atualmente utilizados:

- CPIAUCSL (Consumer Price Index)
- FEDFUNDS (Federal Funds Rate)

---

## Arquitetura ETL

```text
FRED API
    │
    ▼
Extract
(src/extract.py)
    │
    ▼
Transform
(src/transform.py)
    │
    ▼
Load
(src/load.py)
    │
    ▼
Excel Dashboard
(output/macro_dashboard.xlsx)
```

---

## Tecnologias Utilizadas

### Linguagem

- Python 3

### Processamento de Dados

- Pandas

### Integração com APIs

- Requests

### Excel Reporting

- OpenPyXL

### Qualidade e Testes

- Pytest
- unittest.mock

### DevOps

- Git
- GitHub
- GitHub Actions

### Configuração

- python-dotenv

---

## Estrutura do Projeto

```text
macro_etl_portfolio/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── output/
│
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── tests/
│   ├── test_config.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── requirements.txt
├── pyproject.toml
├── pytest.ini
└── README.md
```

---

## Funcionalidades

### Extract

- Conexão à API FRED
- Retry automático para falhas de rede
- Tratamento de erros
- Conversão para DataFrame

### Transform

- Limpeza dos dados
- Cálculo da inflação Year-over-Year
- Preparação dos indicadores para análise

### Load

- Geração automática de dashboard Excel
- Aplicação de formatação profissional
- Ajuste automático de colunas
- Organização visual dos indicadores

---

## Instalação

Clonar o repositório:

```bash
git clone https://github.com/IresBorges/macro_etl_portfolio.git
```

Entrar na pasta:

```bash
cd macro_etl_portfolio
```

Instalar dependências:

```bash
pip install -e .
```

---

## Variáveis de Ambiente

Criar um ficheiro `.env` na raiz do projeto:

```env
FRED_API_KEY=SUA_CHAVE_FRED
```

Obter chave em:

https://fred.stlouisfed.org/

---

## Executar Pipeline

```bash
python -m src.main
```

A pipeline irá:

1. Extrair dados da API FRED
2. Transformar os indicadores
3. Gerar dashboard Excel
4. Produzir logs da execução

---

## Executar Testes

```bash
pytest -v
```

Estado atual:

```text
10 testes aprovados
```

Cobertura:

- Configuração
- Extração
- Transformação
- Geração do dashboard Excel

---

## Integração Contínua

O GitHub Actions executa automaticamente:

```bash
pytest -v
```

em cada:

- Push
- Pull Request

Garantindo que alterações não quebram a pipeline.

---

## Roadmap

### Concluído

- ETL modular
- Logging
- Configuração centralizada
- API FRED
- Dashboard Excel
- Pytest
- GitHub Actions
- CI/CD

### Próximos Passos

- Limpeza de ficheiros transientes do Git
- Aumento da cobertura de testes
- Docker
- Containerização completa da pipeline

---

## Autor

**Ires Borges Neves**

GitHub:

https://github.com/IresBorges