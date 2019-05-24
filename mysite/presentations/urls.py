
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PresentationView.as_view()),
    ]
