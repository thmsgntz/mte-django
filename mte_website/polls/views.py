import os
from enum import Enum, auto

from polls.models import Choice, Question

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


# Create your views here.
class TemplatePathPolls(Enum):
    _PATH = 'polls'
    INDEX = auto()
    DETAIL = auto()

    def __str__(self):
        message = '{0}.html'.format(self.name.lower())
        return os.path.join(self._PATH.value, message)


def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    template = str(TemplatePathPolls.INDEX)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    # try:
    #     question: Question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(f"Question id '{question_id}' does not exist")
    question: Question = get_object_or_404(Question, pk=question_id)
    template = str(TemplatePathPolls.DETAIL)

    return render(request, template, {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """@see: https://docs.djangoproject.com/en/4.1/intro/tutorial04/#write-a-minimal-form."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name.
        # In this case, request.POST['choice'] returns the ID of the selected choice, as a string.
        # request.POST values are always strings.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(
        reverse('polls:results', args=(question.id,)),
    )
