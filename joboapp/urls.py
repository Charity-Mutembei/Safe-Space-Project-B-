from django.urls import path 
from . import views
urlpatterns=[
    path('', views.welcome, name='home'),
    path('/about', views.about, name='about'),
    path('/stories', views.stories, name='stories')
]
