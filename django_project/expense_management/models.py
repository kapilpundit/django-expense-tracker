'''Expense Management App Models'''
from django.db import models
from django.contrib.auth.models import User
from .expense_management_models import ExpenseCategory

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Household Expense')
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.datetime}"
    
    class Meta:
        db_table = 'expense'

