from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('(?P<ques_id>[0-9]+)$', views.question, name='ques'),
    url(r'^success$', views.success_page, name='success_page')
]