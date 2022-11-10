from django.urls import path 
from . import views
urlpatterns=[
    path('', views.welcome, name='home'),
    path('about', views.about, name='about'),
    path('stories', views.stories, name='stories'),
    path ('<str:room>/', views.room, name='room'),
    path ('checkview', views.checkview, name='checkview'),
    path ('send', views.send, name='send'),
    path ('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
