from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # /recipe/712/
    url(r'^(?P<recipe>[0-9]+)/$', views.detail, name='detail'),
]