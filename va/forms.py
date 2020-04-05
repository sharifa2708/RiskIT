from django import forms
from django.forms import ModelForm
from .models import Ques

# CHOICES = (
#     ('H', 'high'),
#     ('M', 'medium'),
#     ('L', 'low'),
# )

class InputForm(forms.ModelForm):
    error_css_class = 'error'

    # choice = forms.ChoiceField(choices=CHOICES, required=True)

    class Meta:
        model = Ques
        fields = '__all__'
