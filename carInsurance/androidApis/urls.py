from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('getPredictions/', views.GetResult().as_view()),
    path('newUser', views.addUser().as_view()),
    path('addCar', views.addCarForUser().as_view()),
    path('payPremium', views.payAmount().as_view()),
    path('buyInsurance', views.buyInsurance().as_view()),


    path('payPremium', views.addUser().as_view()),
    path('payPremium', views.addUser().as_view()),
    path('newUser', views.addUser().as_view()),

]


