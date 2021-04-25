from django.shortcuts import render

def homePage(request):
    context={}
    return render(request, 'base.html', context)

def registerPage(request):
    context = {}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)