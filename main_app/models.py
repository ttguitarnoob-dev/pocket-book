
from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


MONTH_CHOICES = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)

YEAR_CHOICES = (
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
)


# Create your models here.


class Budget(models.Model):
    name = models.CharField(max_length=100, default="New Budget")
    budget_month = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES,
        default='JAN'
    )
    budget_year = models.CharField(
        max_length=5,
        choices=YEAR_CHOICES,
        default='2022'
    )
    base_income = models.IntegerField(default=0)
    additional_income = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.budget_month

    def total_income(self):
        total = self.base_income + self.additional_income
        return total
        
    def total_expenses(self):
        total = 0
        expenses = Expense.objects.filter(budget_id=self.id)
        for thing in expenses:
            total += thing.amount
        return total
    
    def total_leftover(self):
        income = self.base_income + self.additional_income
        total_expenses = 0
        expenses = Expense.objects.filter(budget_id=self.id)
        for thing in expenses:
            total_expenses += thing.amount
        leftover = income - total_expenses
        return leftover




class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    due_date = models.DateField(default=datetime.now)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='expenses')
    
    def __str__(self) -> str:
        return self.name