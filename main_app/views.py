from django.urls import reverse
from django.shortcuts import render
from .models import Budget, Expense
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect


# Create your views here.

# Home


class Home(TemplateView):
    template_name = "home.html"


# Budget List


class BudgetList(TemplateView):
    template_name = "budget_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = Budget.objects.filter(user=self.request.user)

        # name = self.request.GET.get('name')
        # print(self.request)
        # print(name)
        # if name != None:
        #     context['budgets'] = Budget.objects.filter(name__icontains=name)
        # else:
        #     context['']    
        return context

# Create Budget


class CreateBudget(CreateView):
    model = Budget
    fields = ['name', 'budget_month', 'budget_year', 'base_income', 'additional_income']
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


# Create Expense
class ExpenseCreate(CreateView):
    def post(self, request, pk):
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        due_date = request.POST.get("due_date")
        budget = Budget.objects.get(pk=pk)
        Expense.objects.create(name = name, amount = amount, due_date = due_date, budget = budget)
        return redirect('budget_details', pk=pk)
        