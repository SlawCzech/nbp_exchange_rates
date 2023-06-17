import datetime

from django.db import migrations

from ..helpers.initial_data_from_nbp import get_initial_exchange_rates_data


def load_exchange_rates(apps, schema_editor):
    CurrencyName = apps.get_model("exchange_rates", "CurrencyName")
    CurrencyDate = apps.get_model("exchange_rates", "CurrencyDate")
    CurrencyValue = apps.get_model("exchange_rates", "CurrencyValue")

    start_date = datetime.date(2022, 1, 2)
    end_date = datetime.date.today()

    data = get_initial_exchange_rates_data(start_date, end_date)

    exchange_rates = [
        CurrencyValue(
            exchange_rate=rate["mid"],
            currency_name=CurrencyName.objects.get_or_create(name=rate["currency"], code=rate["code"])[0],
            currency_date=CurrencyDate.objects.get_or_create(date=date["effectiveDate"])[0]
        ) for date in data for rate in date["rates"]
    ]

    CurrencyValue.objects.bulk_create(exchange_rates)


def delete_exchange_rates(apps, schema_editor):
    CurrencyName = apps.get_model("exchange_rates", "CurrencyName")
    CurrencyDate = apps.get_model("exchange_rates", "CurrencyDate")
    CurrencyValue = apps.get_model("exchange_rates", "CurrencyValue")

    CurrencyName.objects.all().delete()
    CurrencyDate.objects.all().delete()
    CurrencyValue.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("exchange_rates", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_exchange_rates, delete_exchange_rates)]
