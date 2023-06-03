from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials!")
    
    return render(request, "accounts/login.html")


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Something went wrong :(")

    context = {
        "form": form
    }

    return render(request, "accounts/register.html", context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')