import pytest


@pytest.fixture(scope="function", autouse=True)
def data():
    from src.data_for_tests.data import Data
    data = Data()
    return data
