from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def registerPage(request):
    form = UserCreationForm()
    context = {
        'form':form
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'register.html', context)

def homePage(request):
    context={}
    return render(request, 'base.html', context)
