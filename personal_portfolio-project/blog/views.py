from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    # to show all the objects use Blog.objects.all() here we are ordering the objects by date and showing only last 5
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {"blogs": blogs})
