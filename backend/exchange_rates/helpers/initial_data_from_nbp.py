import datetime
import json
import time
from urllib import request


def get_data_from_nbp(start_date, end_date):
    nbp_api_url = f"http://api.nbp.pl/api/exchangerates/tables/a/{start_date}/{end_date}/"

    with request.urlopen(nbp_api_url) as response:
        data = json.loads(response.read().decode())

    return data


def get_initial_exchange_rates_data(start_date, end_date):
    exchange_rates = []

    while start_date < end_date:
        temp_end_date = start_date + datetime.timedelta(days=90)
        if temp_end_date > end_date:
            temp_end_date = end_date

        temp_data = get_data_from_nbp(start_date, temp_end_date)
        exchange_rates.extend(temp_data)

        start_date = temp_end_date + datetime.timedelta(days=1)

        time.sleep(1)

    return exchange_rates
