from django.shortcuts import render
from .forms import CreateUserForm

def loginPage(request):
    context = {}
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

    return render(request, 'register.html', context)

def homePage(request):
    context={}
    return render(request, 'base.html', context)
