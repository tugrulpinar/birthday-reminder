from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import BirthDayRecord


class BirthDayRecordModelForm(forms.ModelForm):
    class Meta:
        model = BirthDayRecord
        fields = ["name", "date_of_birth"]
        widgets = {"date_of_birth": DatePickerInput()}
