from django.shortcuts import render
from .models import Budget, Expense
from django.views.generic.base import TemplateView


# Create your views here.

# Home
class Home(TemplateView):
    template_name="home.html"

# Budget List
class BudgetList(TemplateView):
    template_name="budget_list.html"