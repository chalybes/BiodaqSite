from django.forms import ModelForm
from django import forms
from .models import Profile


class EntryForms(ModelForm):
    class Meta:
        model = Profile
        exclude = ['PSC', 'slug']

    def clean(self):
        data = self.cleaned_data
        start = data['startDate']
        end = data['endDate']

        if end < start:
            raise forms.ValidationError("Start date cannot be later than end date.")
        else:
            pass

        return data

    fields = ('name', 'mouse', 'startDate', 'endDate',)