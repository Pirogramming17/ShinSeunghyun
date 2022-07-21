from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Post, Devtool

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template_name='posts/home.html', context=context)