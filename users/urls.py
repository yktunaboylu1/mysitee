from django.urls import include, path
from . import views
from django.conf.urls import url
from .views import CustomObtainAuthToken

urlpatterns = [
    path('', views.UserListView.as_view()),
    url(r'^(?P<pk>\d+)$', views.UserDetailView.as_view()),
    url(r'^profiles/$', views.ProfileListView.as_view()),
    url(r'^profiles/(?P<user>\d+)/$', views.ProfileDetailView.as_view()),
    url(r'^login/', CustomObtainAuthToken.as_view()),
]
