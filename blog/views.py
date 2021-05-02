from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    blogs = BlogPost.objects.all()

    return render(request, 'index.html', {'blogs':blogs})


def blog(request, id):
    blogPost = BlogPost.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blogPost})