from django.http import HttpResponse
from django.template import loader

from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    return HttpResponse("Question %s = %s" % (question_id, q))

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s"
        % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)