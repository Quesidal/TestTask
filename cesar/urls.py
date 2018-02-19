from django.conf.urls import url

from . import views

app_name = 'cesar'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^analysis/$', views.analysis),
    url(r'^crypt/$', views.crypt),
    url(r'^decrypt/$', views.decrypt)
]
