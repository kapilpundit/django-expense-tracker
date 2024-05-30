from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='expense-home'),
    path('add-expense/', views.add_expense, name='add-expense'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='expense-about'),
    path('api/response', views.api_response, name='api-response'),
]
