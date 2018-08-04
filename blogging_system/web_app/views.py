from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from blogs.models import Blog


# Create your views here.

def index(request):
    blogs_list = Blog.objects.all()
    context = {'blogs_list': blogs_list}
    return render(request, 'web_app/index.html', context)


def new(request):
    return render(request, 'web_app/new.html')


def create(request):
    try:
        author = request.POST['author']
        print("author: " + author)
        subject = request.POST['subject']
        print("subject: " + subject)
        body = request.POST['body']
        print("body: " + body)
    except KeyError:
        print("KeyError: " + KeyError.__str__())
        return HttpResponseRedirect(reverse('index'))
    else:
        Blog.objects.create(author=author, subject=subject, body=body)
        return HttpResponseRedirect(reverse('index'))
