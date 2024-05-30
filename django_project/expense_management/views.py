'''
Blog app's views
'''
import json
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from django.conf import settings
from django.http import HttpResponse
from .models import Expense
from .expense_management_models import ExpenseCategory
from .forms.login import LoginForm
from .forms.expense_form import ExpenseForm


# Create your views here.
@login_required
def home(request):
    '''
    Home Page
    Show listing of all expenses
    '''
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    expenses = Expense.objects.all()
    if start_date and end_date:
        expenses = expenses.filter(datetime__range=[parse_date(start_date), parse_date(end_date)])

    context = {
        'request': request,
        'expenses': expenses,
        'EXPENSE_MANAGEMENT_TITLE': settings.EXPENSE_MANAGEMENT_TITLE
    }

    return render(request, 'partials/home.html', context)

@login_required
def add_expense(request):
    # Get all ExpenseCategory objects
    categories = ExpenseCategory.objects.all()
    excluded_usernames = ['admin', 'another_user']
    users = User.objects.exclude(username__in=excluded_usernames)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            print('Expense', expense)
            return redirect('expense-home')  # Redirect to the home page after successful submission
        else:
            # Print form errors if the form is not valid
            print(form.errors)
            print(form.data)
    else:
        form = ExpenseForm()

    context = {
        'request': request,
        'form': form,
        'categories': categories,
        'users': users,
        'EXPENSE_MANAGEMENT_TITLE': settings.EXPENSE_MANAGEMENT_TITLE
    }

    return render(request, 'partials/add_expense.html', context)

def user_login(request):
    '''
    User login form
    '''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or homepage
                return redirect('expense-home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    '''Logout user'''
    logout(request)
    # Redirect to the login page or any other page
    return redirect('login')  # Change 'login' to your login URL name

def about(request):
    '''About Page'''
    return render(request, 'blog/about.html', {'title': 'About'})

def api_response(request):
    '''Api Response view'''
    context = {
        'status': 'success',
        'httpCode': 200,
        'data': 'Hi, I am an HttpResponse Object'
    }

    return HttpResponse(json.dumps( context ), status=201)
