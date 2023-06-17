import datetime

from django import forms


class ExchangeRateForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "min": "2023-01-01"}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "max": str(datetime.date.today())}))
    currency = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date > end_date:
            self.add_error("end_date", "End date cannot be earlier than start date.")

        return cleaned_data
