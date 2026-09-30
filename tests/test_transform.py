import pandas as pd

import src.config as config
import src.transform as transform


def test_transform_logic(tmp_path, monkeypatch):
    """
    Testa o cálculo da inflação YoY e a limpeza de nulos.
    """

    dates = pd.date_range(
        start="2025-01-01",
        periods=14,
        freq="MS"
    )

    cpi_values = [
        300.0 + i for i in range(14)
    ]

    fed_values = [
        3.5 for _ in range(14)
    ]

    df_mock = pd.DataFrame(
        {
            "date": dates,
            "CPIAUCSL": cpi_values,
            "FEDFUNDS": fed_values
        }
    )

    raw_dir = tmp_path / "raw"
    proc_dir = tmp_path / "processed"

    raw_dir.mkdir()
    proc_dir.mkdir()

    monkeypatch.setattr(
        config,
        "DATA_RAW_DIR",
        str(raw_dir)
    )

    monkeypatch.setattr(
        config,
        "DATA_PROC_DIR",
        str(proc_dir)
    )

    monkeypatch.setattr(
        transform,
        "DATA_RAW_DIR",
        str(raw_dir)
    )

    monkeypatch.setattr(
        transform,
        "DATA_PROC_DIR",
        str(proc_dir)
    )

    input_file = raw_dir / "macro_raw.csv"

    df_mock.to_csv(
        input_file,
        index=False
    )

    df_result = (
        transform
        .transform_macro_data()
    )

    assert (
        "CPI_Inflation_YoY"
        in df_result.columns
    )

    assert (
        "Interest_Rate"
        in df_result.columns
    )

    assert len(df_result) == 2

    assert not (
        df_result
        .isnull()
        .any()
        .any()
    )