import logging
import os
import pandas as pd

from src.config import (
    DATA_RAW_DIR,
    DATA_PROC_DIR,
    LOGS_DIR
)

logger = logging.getLogger("ETL_Transform")


def transform_macro_data() -> pd.DataFrame:
    """
    Lê os dados brutos, calcula a inflação YoY,
    trata valores nulos e exporta os dados processados.
    """

    input_path = os.path.join(
        DATA_RAW_DIR,
        "macro_raw.csv"
    )

    output_path = os.path.join(
        DATA_PROC_DIR,
        "macro_transformed.csv"
    )

    if not os.path.exists(input_path):

        logger.error(
            f"Ficheiro não encontrado: {input_path}"
        )

        raise FileNotFoundError(
            f"Ficheiro não encontrado: {input_path}"
        )

    logger.info(
        "Iniciando transformação dos dados."
    )

    df = pd.read_csv(
        input_path,
        parse_dates=["date"]
    )

    df = df.set_index("date")

    df["CPI_Inflation_YoY"] = (
        df["CPIAUCSL"].pct_change(12) * 100
    )

    df["Interest_Rate"] = df["FEDFUNDS"]

    df_transformed = (
        df[
            [
                "CPI_Inflation_YoY",
                "Interest_Rate"
            ]
        ]
        .dropna()
        .reset_index()
    )

    os.makedirs(
        DATA_PROC_DIR,
        exist_ok=True
    )

    df_transformed.to_csv(
        output_path,
        index=False
    )

    logger.info(
        f"Transformação concluída: "
        f"{output_path}"
    )

    logger.info(
        f"Registos processados: "
        f"{len(df_transformed)}"
    )

    return df_transformed


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(
                os.path.join(
                    LOGS_DIR,
                    "pipeline.log"
                ),
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ]
    )

    transform_macro_data()