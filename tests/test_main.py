import os
import pytest
import polars as pl
from src.main import get_file_size, read_parquet, get_data_info

def test_get_file_size():
    size = get_file_size('droids.parquet')
    assert size > 0

def test_read_parquet():
    df = read_parquet('droids.parquet')
    assert isinstance(df, pl.DataFrame)

def test_get_data_info():
    df = read_parquet('droids.parquet')
    info = get_data_info(df)
    assert 'rows' in info and 'columns' in info

def test_log_file_exists():
    log_file = 'app.log'
    assert os.path.exists(log_file), "Log file does not exist"

def test_log_file_not_empty():
    log_file = 'app.log'
    size = os.path.getsize(log_file)
    assert size > 0, "Log file is empty"
