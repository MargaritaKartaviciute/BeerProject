from django import forms

class BreweriesForm(forms.Form):
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()