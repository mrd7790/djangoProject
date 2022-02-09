from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'BLog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'BLog Post 2',
        'content': 'second Post Content',
        'date_posted': 'August 28, 2022'
    }
]


def home(request):
    contex = {
        'posts': posts
    }
    return render(request, 'blog/home.html', contex)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
# Create your views here.
