from django.shortcuts import render, get_object_or_404
from .models import Blog

app_name = 'blog'


def all_blogs(request):
    # to show all the objects use Blog.objects.all() here we are ordering the objects by date and showing only last 5
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {"blogs": blogs})


def blog_details(request, blog_id):
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_details.html', {"blog_object": blog_object})