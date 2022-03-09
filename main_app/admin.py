from django.contrib import admin

# from main_app.models import Budget

from .models import Budget, Expense

# Register your models here.

admin.site.register(Budget)
admin.site.register(Expense)