# expense_management/models/expense_category.py
from django.db import models
from django.utils import timezone

class ExpenseCategory(models.Model):
    '''Expense Category Model'''
    category = models.CharField(max_length=50)
    slug = models.CharField(max_length=150, default='')
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return f"{self.category}"
    
    class Meta:
        db_table = 'expense_categories'
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"