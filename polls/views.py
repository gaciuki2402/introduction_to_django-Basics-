from email.policy import HTTP
from django.shortcuts import render

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

 
    

# Create your views here.
