# expense_management/forms.py
from django import forms
from ..models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'datetime', 'category', 'user', 'description']
