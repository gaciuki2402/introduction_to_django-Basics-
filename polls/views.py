from django.shortcuts import render
<<<<<<< HEAD
from .models import Post


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'polls/home.html', context)

def about(request):
    return render(request, 'polls/about.html', {'title':'about'})

=======
from django.http import HttpResponse
<<<<<<< HEAD
def index(request):
    context={}
    return render(request, "polls/index.html",context)

def about(request):
    context={}
    return render(request, "polls/about.html",context)

=======

def lib(request):
    return HttpResponse("Hello,Welcome to the Libray.It's open 24/7")
    
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d

# Create your views here.
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
