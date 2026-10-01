import pytest
from unittest.mock import patch, MagicMock

import pandas as pd
import requests

from src.extract import (
    create_resilient_session,
    fetch_fred_series
)


def test_resilient_session_adapters():
    """
    Valida a criação da sessão resiliente.
    """

    session = create_resilient_session()

    assert isinstance(
        session,
        requests.Session
    )

    assert "https://" in session.adapters

    assert "http://" in session.adapters


@patch("src.extract.requests.Session.get")
def test_fetch_fred_series_success(mock_get):
    """
    Testa a resposta bem-sucedida da API.
    """

    mock_response = MagicMock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "observations": [
            {
                "date": "2026-01-01",
                "value": "100.5"
            },
            {
                "date": "2026-02-01",
                "value": "101.0"
            }
        ]
    }

    mock_get.return_value = mock_response

    df = fetch_fred_series("CPIAUCSL")

    assert isinstance(
        df,
        pd.DataFrame
    )

    assert "CPIAUCSL" in df.columns

    assert len(df) == 2

    assert df.index.name == "date"

    assert df.iloc[0]["CPIAUCSL"] == 100.5


@patch("src.extract.requests.Session.get")
def test_fetch_fred_series_api_error(mock_get):
    """
    Testa falha HTTP da API.
    """

    mock_response = MagicMock()

    mock_response.status_code = 500

    mock_get.return_value = mock_response

    with pytest.raises(RuntimeError):
        fetch_fred_series("CPIAUCSL")


@patch("src.extract.requests.Session.get")
def test_fetch_fred_series_empty_observations(mock_get):
    """
    Testa payload vazio da API.
    """

    mock_response = MagicMock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "observations": []
    }

    mock_get.return_value = mock_response

    with pytest.raises(ValueError):
        fetch_fred_series("CPIAUCSL")