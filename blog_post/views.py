from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
# Create your views here.

@login_required(login_url='login')
def newPostPage(request):
    context = {}

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = BlogPost(
            title = title,
            content = content,
            creator = request.user
        )
        post.save()
        return redirect('home')

    return render(request, 'newPost.html' ,context)