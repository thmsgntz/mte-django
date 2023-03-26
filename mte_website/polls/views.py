import os
from enum import Enum

from polls.models import Choice, Question

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


class TemplatePolls(Enum):
    """Enum pour Polls urls."""

    app_name = 'polls'
    index = 'index'
    detail = 'detail'
    result_s = 'results'

    def to_html(self):
        """Generate path 'polls/x.html' in templates.

        Used in render: >> render(request,
        TemplatePolls.index.to_html(), context)
        """
        message = '{0}.html'.format(self.value.lower())
        return os.path.join(self.app_name.value, message)

    def to_reverse(self):
        """Generate 'polls:x'.

        Usage in reverse:
        >> HttpResponseRedirect(reverse(TemplatePolls.index.to_reverse(), args=())
        """
        return '{0}:{1}'.format(self.app_name.value.lower(), self.value.lower())


def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    template = TemplatePolls.index.to_html()

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    # try:
    #     question: Question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(f"Question id '{question_id}' does not exist")
    question: Question = get_object_or_404(Question, pk=question_id)
    return render(request, TemplatePolls.detail.to_html(), {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, TemplatePolls.result_s.to_html(), {'question': question})


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
            request, TemplatePolls.detail.to_html(), {
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
        reverse(TemplatePolls.result_s.to_reverse(), args=(question.id,)),
    )
