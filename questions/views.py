from django.conf.urls import url
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render
from questions import urls
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from questions.models import Question, Answer, Tag, Vote

questions_per_page = 3

QUESTIONS = {
    '1': {'id': 1, 'rating': 2, 'title': 'I`m your dream', 'text': 'I`m your dream, make you real', 'author': 'Jury Golubev', 'tags': ['Java', 'Python', 'C++']},
    '2': {'id': 2, 'rating': 8, 'title': 'I`m your eyes', 'text': 'I`m your eyes when you must steal', 'author': 'Dr.Pepper', 'tags': ['R', 'Ruby', 'C++']},
    '3': {'id': 3, 'rating': 3, 'title': 'I`m your pain', 'text': 'I`m your pain when you can`t feel', 'author': 'Mary Poppins', 'tags': ['Go', 'Swift', 'C++']},
}
loggedin = True


class AboutView(TemplateView):
    template_name = "about.html"


def questions_new(request, **kwargs):
    pk = kwargs.get('pk', 1) or 1
    # if pk is None or int(pk) < 1:
    #     pk = 1
    questions, paginator = select_page(Question.objects.new().all(), pk)
    paginator.base_url = '/'
    return render(request, "questions_new.html", {'questions': questions, 'paginator': paginator, 'page': int(pk)})


def select_page(item_list, page):
    paginator = Paginator(item_list, questions_per_page)
    try:
        return paginator.page(page), paginator
    except PageNotAnInteger:
        raise Http404("Page number is not an integer")
    except EmptyPage:
        return paginator.page(paginator.num_pages), paginator


def about(request):
    data = []
    if request.method == 'GET':
        data = request.GET
    if request.method == 'POST':
        data = request.POST
    return render(request, 'about.html',
                  {'method': request.method,
                   'data': data})



def questions_hot(request, **kwargs):
    pk = kwargs.get('pk', 1) or 1
    questions, paginator = select_page(Question.objects.hot(), pk)
    paginator.baseurl = reverse("questions_hot")
    return render(request, "questions_hot.html", {'questions': questions, 'paginator': paginator, 'page': pk})


def question_detail(request, **kwargs):
    pk = kwargs.get('pk', 1)
    pk = int(pk)
    question = Question.objects.get(pk=pk)
    return render(request, 'question_detail.html', {'question': question, 'loggedin': loggedin})


def questions_by_tag(request, **kwargs):
    tag = kwargs.get('tag', 1)
    pk = kwargs.get('pk', 1) or 1
    if not tag:
        raise Http404("No tag provided")
    questions, paginator = select_page(Question.objects.by_tag(tag), pk)
    paginator.baseurl = reverse("questions_by_tag", kwargs={'tag': tag})
    return render(request, 'tags.html', {'questions': questions, 'paginator': paginator, 'page': pk})


def settings(request):
    return render(request, 'settings.html', {'loggedin': loggedin})


def signup(request):
    return render(request, 'signup.html', {'loggedin': False})


def authorization(request):
    return render(request, 'authorization.html', {'loggedin': False})


def ask(request):
    return render(request, 'ask.html', {'loggedin': True})