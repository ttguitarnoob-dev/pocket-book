from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('budgets/', views.BudgetList.as_view(), name='budget_list'),
    path('budgets/new/', views.CreateBudget.as_view(), name='create_budget'),
    path('budgets/<int:pk>/,', views.BudgetDetail.as_view(), name='budget_details'),
    path('budgets/<int:pk>/update/', views.BudgetUpdate.as_view(), name="budget_update"),
    path('budgets/<int:pk>/delete', views.BudgetDelete.as_view(), name="budget_delete"),
]