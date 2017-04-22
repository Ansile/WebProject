from django.conf.urls import url

from questions.views import AboutView
from questions.views import questions_new, questions_detail, settings, signup, hot, ask, authorization, tags

urlpatterns = [
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^$', questions_new, name='questions_new'),
    url(r'^settings/$', settings, name='settings'),	
    url(r'^signup/$', signup, name='signup'),	
    url(r'^hot/$', hot, name='hot'),	
    url(r'^ask/$', ask, name='ask'),	
    url(r'^tag/$', tags, name='tags'),
    url(r'^authorization/$', authorization, name='authorization'),						
]

