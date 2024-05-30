from django.contrib import admin
from .models import Expense
from .expense_management_models import ExpenseCategory

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    '''Register Expense Model in Admin Panel'''
    list_display = ('user', 'datetime', 'category', 'amount')
    list_filter = ('category', 'datetime')
    search_fields = ('description',)

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    '''Register ExpenseCategory Model in Admin Panel'''
    list_display = ('category', 'created_at', 'updated_at')
