import datetime

import pytest


@pytest.fixture
def start_date():
    return datetime.date(2023, 6, 15)


@pytest.fixture
def end_date():
    return datetime.date(2023, 6, 16)


@pytest.fixture
def first_jan():
    return datetime.date(2022, 1, 1)


@pytest.fixture
def last_dec():
    return datetime.date(2022, 12, 31)
