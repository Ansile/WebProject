from django.conf.urls import url

from questions import views

urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^(?:(?P<pk>\d+)/)?$', views.questions_new, name='questions_new'),
    url(r'^question/(?:(?P<pk>\d+)/)?$', views.question_detail, name='question_detail'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^hot/(?:(?P<pk>\d+)/)?$', views.questions_hot, name='questions_hot'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^tag/(?:(?P<tag>\w+)/)(?:(?P<pk>\d+)/)?$', views.questions_by_tag, name='questions_by_tag'),
    url(r'^authorization/$', views.authorization, name='authorization'),
]
