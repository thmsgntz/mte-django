import os
from enum import Enum, auto

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


# Create your views here.
class TemplatePathPolls(Enum):
    _PATH = "polls"
    INDEX = auto()
    DETAIL = auto()

    def __str__(self):
        return os.path.join(self._PATH.value, self.name.lower() + ".html")


def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    template = str(TemplatePathPolls.INDEX)

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    # try:
    #     question: Question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(f"Question id '{question_id}' does not exist")
    question: Question = get_object_or_404(Question, pk=question_id)
    template = str(TemplatePathPolls.DETAIL)

    return render(request, template, {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
