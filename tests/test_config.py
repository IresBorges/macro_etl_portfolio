import os

from src.config import (
    BASE_DIR,
    DATA_RAW_DIR,
    DATA_PROC_DIR,
    OUTPUT_DIR,
    LOGS_DIR,
    FRED_API_KEY
)


def test_directories_existence():
    assert os.path.exists(DATA_RAW_DIR)
    assert os.path.exists(DATA_PROC_DIR)
    assert os.path.exists(OUTPUT_DIR)
    assert os.path.exists(LOGS_DIR)


def test_base_dir_is_absolute():
    assert os.path.isabs(BASE_DIR)


def test_api_key_loaded():
    assert FRED_API_KEY is not None
    assert isinstance(FRED_API_KEY, str)
    assert len(FRED_API_KEY) > 0
