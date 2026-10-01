import os

import pandas as pd
import pytest

from src.load import generate_excel_dashboard
from src.config import (
    DATA_PROC_DIR,
    OUTPUT_DIR
)


def test_generate_excel_dashboard_success():
    """
    Valida a geração do ficheiro Excel.
    """

    input_file = os.path.join(
        DATA_PROC_DIR,
        "macro_transformed.csv"
    )

    test_df = pd.DataFrame(
        {
            "date": ["2026-01-01"],
            "CPI_Inflation_YoY": [2.3],
            "Interest_Rate": [4.5]
        }
    )

    test_df.to_csv(
        input_file,
        index=False
    )

    generate_excel_dashboard()

    output_file = os.path.join(
        OUTPUT_DIR,
        "macro_dashboard.xlsx"
    )

    assert os.path.exists(
        output_file
    )


def test_generate_excel_dashboard_missing_file():
    """
    Valida erro quando o CSV de entrada
    não existe.
    """

    input_file = os.path.join(
        DATA_PROC_DIR,
        "macro_transformed.csv"
    )

    if os.path.exists(input_file):
        os.remove(input_file)

    with pytest.raises(
        FileNotFoundError
    ):
        generate_excel_dashboard()