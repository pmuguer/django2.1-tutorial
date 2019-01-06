from django.http import HttpResponse, Http404
from django.shortcuts import render

from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {'question': q})

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s"
        % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)