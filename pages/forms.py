from django import forms

from .models import BirthDayRecord


class BirthDayRecordModelForm(forms.ModelForm):
    class Meta:
        model = BirthDayRecord
        fields = ["name", "date_of_birth"]
