import os
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")

if not FRED_API_KEY:
    raise ValueError(
        "A variável de ambiente FRED_API_KEY não foi encontrada. Verifique o ficheiro .env."
    )

# Diretórios base do projeto
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_RAW_DIR = os.path.join(
    BASE_DIR,
    "data",
    "raw"
)

DATA_PROC_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)

LOGS_DIR = os.path.join(
    BASE_DIR,
    "logs"
)

# Garantir que as pastas essenciais existem
for path in [
    DATA_RAW_DIR,
    DATA_PROC_DIR,
    OUTPUT_DIR,
    LOGS_DIR
]:
    os.makedirs(path, exist_ok=True)