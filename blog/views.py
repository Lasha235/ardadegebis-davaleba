from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 22, 2026'
    },
    {
        'author': 'John Pork',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 23, 2026'
    },
]



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
