from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('getPredictions/', views.GetResult().as_view()),
    path('trial', views.inbuilt),
    path('newUser', views.addUser().as_view()),
]
