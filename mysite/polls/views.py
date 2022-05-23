from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f'You\'re looking at question results {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')