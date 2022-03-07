from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('budgets/', views.BudgetList.as_view(), name='budget_list'),
]