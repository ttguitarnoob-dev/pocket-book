from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View


# Create your views here.
# class Signup(View):
#     def get(self, request):
#         form = UserCreationForm()
#         context = {'form': form}
#         return render(request, 'accounts/signup.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('budget_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})