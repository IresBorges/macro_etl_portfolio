import logging
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd

from src.config import (
    FRED_API_KEY,
    DATA_RAW_DIR,
    LOGS_DIR
)

# Configuração do logging
log_file = os.path.join(LOGS_DIR, "pipeline.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ETL_Extract")


def create_resilient_session() -> requests.Session:
    """
    Cria uma sessão HTTP com retry automático
    para maior resiliência de rede.
    """

    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[
            429,
            500,
            502,
            503,
            504
        ],
        raise_on_status=False
    )

    adapter = HTTPAdapter(
        max_retries=retry_strategy
    )

    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session


def fetch_fred_series(series_id: str) -> pd.DataFrame:
    """
    Extrai uma série temporal da API do FRED.
    """

    url = (
        "https://api.stlouisfed.org/"
        "fred/series/observations"
    )

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json"
    }

    logger.info(
        f"Iniciando extração da série {series_id}"
    )

    session = create_resilient_session()

    try:

        response = session.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code != 200:

            logger.error(
                f"Erro API {series_id} "
                f"Status={response.status_code}"
            )

            raise RuntimeError(
                f"Erro na série {series_id}"
            )

        data = response.json().get(
            "observations",
            []
        )

        if not data:

            logger.warning(
                f"Nenhum dado encontrado "
                f"para {series_id}"
            )

            raise ValueError(
                f"Nenhum dado encontrado "
                f"para {series_id}"
            )

        df = pd.DataFrame(data)[
            ["date", "value"]
        ]

        df["value"] = pd.to_numeric(
            df["value"],
            errors="coerce"
        )

        df["date"] = pd.to_datetime(
            df["date"]
        )

        df_cleaned = (
            df.dropna()
              .rename(
                  columns={
                      "value": series_id
                  }
              )
              .set_index("date")
        )

        logger.info(
            f"Série {series_id} carregada "
            f"com {len(df_cleaned)} registros"
        )

        return df_cleaned

    except requests.exceptions.RequestException as e:

        logger.exception(
            f"Erro de rede ao consultar "
            f"a série {series_id}"
        )

        raise e


if __name__ == "__main__":

    indicators = [
        "CPIAUCSL",
        "FEDFUNDS"
    ]

    dfs = []

    for series in indicators:

        df_series = fetch_fred_series(series)

        dfs.append(df_series)

    macro_df = pd.concat(
        dfs,
        axis=1
    ).dropna()

    output_path = os.path.join(
        DATA_RAW_DIR,
        "macro_raw.csv"
    )

    macro_df.to_csv(output_path)

    logger.info(
        f"Dados gravados com sucesso em: "
        f"{output_path}"
    )