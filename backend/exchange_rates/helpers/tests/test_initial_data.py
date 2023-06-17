import datetime

from ..initial_data_from_nbp import get_data_from_nbp, get_initial_exchange_rates_data


def test_get_custom_data_from_nbp(start_date, end_date):
    data = get_data_from_nbp(start_date, end_date)

    assert len(data) == 2
    assert data[0]['effectiveDate'] == datetime.date.strftime(start_date, "%Y-%m-%d")
    assert data[1]['effectiveDate'] == datetime.date.strftime(end_date, "%Y-%m-%d")


def test_get_custom_data_from_longer_period(first_jan, last_dec):
    data = get_initial_exchange_rates_data(first_jan, last_dec)

    assert len(data) == 252

