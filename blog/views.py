from django.shortcuts import render
from.models import Post

posts = [
    {
        'author': 'Gurpreet Cheema',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 1st, 2018'
    },
    {
        'author': 'Gurpreet Kaur',
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 2nd, 2018'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
