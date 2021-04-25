from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Hibás felhasználónév vagy jelszó!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()
    context = {
        'form':form
    }

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + " felhasználó létrejött!")
            return redirect('login')

    return render(request, 'register.html', context)

@login_required(login_url='login')
def homePage(request):
    context={}
    return render(request, 'base.html', context)
