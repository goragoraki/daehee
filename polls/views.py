from django import template
from django import http
from polls.models import Question
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response
from django.template import loader
from .models import Question
# Create your views here.

def index(request):
    # 1
    # return HttpResponse("hello in polls")
    # 2
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output =', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    #3
    #latest_question_list =Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

    #4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html' , context)


def detail(request, question_id):
    # 1
    # return HttpResponse("you're looking at the results of question %s." # % question_id)

    #2
    #try: 
    #   question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise response.Http404("Question does not exist")
    #return render(request, "polls/detail.html",{'question': question})

    #3
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response ="you're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)