from django.shortcuts import render

from .models import Choice, Questions and Choice

def index(request):
    return render(request, 'poll/sindex.html')
    

# Create your views here.
