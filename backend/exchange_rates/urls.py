from django.urls import path

from . import views

app_name = "exchange_rates"

urlpatterns = [
    path("", views.ExchangeRateFormView.as_view(), name="exchange_rate_form"),
]
