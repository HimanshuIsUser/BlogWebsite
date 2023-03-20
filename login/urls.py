from django.urls import path
from .views import *
urlpatterns = [
    path('login/',Login.as_view()),
    path('register-page/',register),
    path('register/',Shop_registrations_view.as_view()),
    path('user-register/',User_register.as_view()),
]
