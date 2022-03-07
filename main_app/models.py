from email.policy import default
from django.db import models

MONTH_CHOICES = (
    ('JAN', 'January'),
    ('FEB', 'February'),
    ('MAR', 'March'),
    ('APR', 'April'),
    ('MAY', 'May'),
    ('JUN', 'June'),
    ('JUL', 'July'),
    ('AUG', 'August'),
    ('SEP', 'September'),
    ('OCT', 'October'),
    ('NOV', 'November'),
    ('DEC', 'December'),
)

# Create your models here.


class Budget(models.Model):
    name = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES,
        default='JAN'
    )
    base_income = models.IntegerField(default=0)
    additional_income = models.IntegerField(default=0)
    # Year Add later

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    due_date = models.IntegerField(default=0)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name