from django.conf.urls import url

from questions.views import AboutView
from questions.views import questions_list, questions_detail, settings

urlpatterns = [
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^$', questions_list, name='questions_list'),
    url(r'^settings/$', settings, name='settings'),		
]

