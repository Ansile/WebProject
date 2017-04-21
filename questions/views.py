from django.views.generic import TemplateView
from django.shortcuts import render

QUESTIONS = {
    '1': {'id': 1, 'rating': 2, 'title': 'I`m your dream', 'text': 'I`m your dream, make you real', 'author': 'Jury Golubev', 'tags': ['Java', 'Python', 'C++']},
    '2': {'id': 2, 'rating': 8, 'title': 'I`m your eyes', 'text': 'I`m your eyes when you must steal', 'author': 'Dr.Pepper', 'tags': ['R', 'Ruby', 'C++']},
    '3': {'id': 3, 'rating': 3,'title': 'I`m your pain', 'text': 'I`m your pain when you can`t feel', 'author': 'Mary Poppins', 'tags': ['Go', 'Swift', 'C++']},
}
loggedin = True

class AboutView(TemplateView):
    template_name = "about.html"


def about(request):
    data = []
    if request.method == 'GET':
        data = request.GET
    if request.method == 'POST':
        data = request.POST
    return render(request, 'about.html',
                  {'method': request.method,
                   'data': data})

def questions_list(request):
    return render(request, 'questions_list.html', {'questions': QUESTIONS.values(), 'loggedin': loggedin})


def questions_detail(request, question_id):
    return render(request, 'questions_detail.html', {'question': QUESTIONS.get(question_id, {}), 'loggedin': loggedin})

def settings(request):
    return render(request, 'settings.html', {'questions': QUESTIONS.values(), 'loggedin': loggedin})
