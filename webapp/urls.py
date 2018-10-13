from django.urls import include, path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
]
