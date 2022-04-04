<<<<<<< HEAD
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
=======
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questions,Choice

#get questions and display them
def index(request):
    latest_question_list=Questions.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request, "polls/index.html", context)

#show specific question and choices
def detail(request, question_id):
    try:
        question=Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question Does not exist")
    return render(request,"polls/results.html", {'question': question})

#get question and display results
def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id )
    return render(request, "polls/results.html", { "question":question})

#vote for a question choice
def vote(request,question_id):
    #print(request.POST['choice'])
    question=get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return ana HttResponseRedirect after successfully dealing
        # with POST data.This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
>>>>>>> c5cfede35fded4403fe8b335a6b75cf8207eecfa
