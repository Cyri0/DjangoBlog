from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog_post.models import BlogPost

@login_required(login_url='login')
def homePage(request):
    posts = BlogPost.objects.filter()
    context={
        'posts':posts
    }
    return render(request, 'base.html', context)