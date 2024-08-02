from django.http import HttpResponse
from django.http import Http404
# from django.template import loader
from django.shortcuts import render

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_data")
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    # 第二种快捷方式 可以解决HttpResponse 和 loader的依赖
    return render(request,"polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questionn does not exist")
    # 快速的提供一个404报错 shortcuts的函数
    # question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
