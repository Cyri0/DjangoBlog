from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    print('Futok!')
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', context)


def registerPage(request):
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

def homePage(request):
    context={}
    return render(request, 'base.html', context)
