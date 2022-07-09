from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import *

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # q = Question.objects.get(id=2)
    return render(request, 'index.html', {'latest_question_list':latest_question_list})

# question_id도 인자로 받아와서 사용.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 모델명(소문자)_set 으로 
    choice_list = question.choice_set.all()
    return render(request, 'detail.html', {'question':question ,'choice_list': choice_list})
    # return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)