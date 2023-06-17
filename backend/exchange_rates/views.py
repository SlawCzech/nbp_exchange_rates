from django.views.generic import FormView

from . import forms, models


class ExchangeRateFormView(FormView):
    template_name = 'exchange_rates/exchange_rate_view.html'
    form_class = forms.ExchangeRateForm

    def get_form(self, form_class=None):
        currencies = models.CurrencyName.objects.all()
        form = super().get_form(form_class)

        form.fields["currency"].choices = [(currency.code, currency.name.capitalize()) for currency in currencies]

        return form
