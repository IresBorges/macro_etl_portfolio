import logging
import os
import time

import pandas as pd

from src.config import (
    LOGS_DIR,
    DATA_RAW_DIR
)

from src.extract import fetch_fred_series
from src.transform import transform_macro_data
from src.load import generate_excel_dashboard


log_file = os.path.join(
    LOGS_DIR,
    "pipeline.log"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(
            log_file,
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(
    "ETL_Orchestrator"
)


def run_pipeline() -> None:

    start_time = time.time()

    logger.info("=" * 50)
    logger.info(
        "INÍCIO DA EXECUÇÃO DO PIPELINE"
    )
    logger.info("=" * 50)

    try:

        logger.info(
            "[ETAPA 1/3] EXTRAÇÃO"
        )

        indicators = [
            "CPIAUCSL",
            "FEDFUNDS"
        ]

        dfs = []

        for series in indicators:

            df_series = fetch_fred_series(
                series
            )

            dfs.append(df_series)

        macro_df = pd.concat(
            dfs,
            axis=1
        ).dropna()

        raw_output_path = os.path.join(
            DATA_RAW_DIR,
            "macro_raw.csv"
        )

        macro_df.to_csv(
            raw_output_path
        )

        logger.info(
            "[ETAPA 1/3] CONCLUÍDA"
        )

        logger.info(
            "[ETAPA 2/3] TRANSFORMAÇÃO"
        )

        transform_macro_data()

        logger.info(
            "[ETAPA 2/3] CONCLUÍDA"
        )

        logger.info(
            "[ETAPA 3/3] LOAD"
        )

        generate_excel_dashboard()

        logger.info(
            "[ETAPA 3/3] CONCLUÍDA"
        )

        elapsed = (
            time.time() - start_time
        )

        logger.info("=" * 50)

        logger.info(
            f"PIPELINE CONCLUÍDO EM "
            f"{elapsed:.2f} SEGUNDOS"
        )

        logger.info("=" * 50)

    except Exception as e:

        logger.critical(
            f"FALHA CRÍTICA: {e}",
            exc_info=True
        )

        raise


if __name__ == "__main__":
    run_pipeline()