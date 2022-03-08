from django.urls import reverse
from django.shortcuts import render
from .models import Budget, Expense
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


# Create your views here.

# Home


class Home(TemplateView):
    template_name = "home.html"


# Budget List


class BudgetList(TemplateView):
    template_name = "budget_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = Budget.objects.all()
        return context

# Create Budget


class CreateBudget(CreateView):
    model = Budget
    fields = ['budget_month', 'base_income', 'additional_income']
    template_name = "create_budget.html"
    success_url = "/budgets/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBudget, self).form_valid(form)

    def get_success_url(self):
        return reverse('budget_details', kwargs={'pk': self.object.pk})

# Detail Page


class BudgetDetail(DetailView):
    model = Budget
    template_name = "budget_detail.html"

    

        # Update Budget


class BudgetUpdate(UpdateView):
    model = Budget
    fields = ['budget_month', 'base_income', 'additional_income']
    template_name = "budget_update.html"
    success_url = "/budgets/"


# Delete Budget

class BudgetDelete(DeleteView):
    model = Budget
    template_name = "budget_delete_confirmation.html"
