from django import forms
from .models import Expenses, exp_category

class ExpensesForm(forms.ModelForm):
    class Meta:
        model=Expenses
        fields=["name","amount","exp_type"]
        #fields=["name"]

class UserForm(forms.Form):
        name = forms.CharField(max_length=100)
        amount = forms.CharField(max_length=100)
        exp_type = forms.CharField(label='What is your expense type', widget=forms.Select(choices=exp_category))
