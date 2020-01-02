from django import forms

class BreweriesForm(forms.Form):
    latitude = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your latitude...'
        }
    ))
    longitude = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your longitude...'
        }
    ))