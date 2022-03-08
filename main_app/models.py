
from datetime import datetime
from email.policy import default
from django.db import models

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

# Create your models here.


class Budget(models.Model):
    budget_month = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES,
        default='JAN'
    )
    base_income = models.IntegerField(default=0)
    additional_income = models.IntegerField(default=0)
    # Year Add later

    def __str__(self) -> str:
        return self.budget_month

    def total_income(self):
        total = self.base_income + self.additional_income
        return total

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    due_date = models.DateField(default=datetime.now)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='expenses')
    
    def __str__(self) -> str:
        return self.name

    