from django.views.generic import FormView
from django.core import serializers
from . import forms, models


class ExchangeRateFormView(FormView):
    template_name = 'exchange_rates/exchange_rate_view.html'
    form_class = forms.ExchangeRateForm
    success_url = "/"

    def get_form(self, form_class=None):
        currencies = models.CurrencyName.objects.all()
        form = super().get_form(form_class)

        form.fields["currency"].choices = [(currency.code, currency.name.capitalize()) for currency in currencies]

        return form

    def form_valid(self, form):
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        currencies = form.cleaned_data.get("currency")

        dates = models.CurrencyDate.objects.filter(date__range=(start_date, end_date))

        currency_data = models.CurrencyValue.objects.filter(currency_date__date__range=(start_date, end_date),
                                                            currency_name__code__in=currencies)

        data = {
            "labels": [date.date.strftime("%Y-%m-%d") for date in dates],
            "datasets": [{
                "label": currency,
                "data": [
                    float(value.exchange_rate) for value in currency_data if value.currency_name.code == currency
                ]
            } for currency in currencies]
        }

        context = self.get_context_data()
        context.update({"currency_data": currency_data})
        context.update({"data": data})

        return self.render_to_response(context)
