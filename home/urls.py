from .views import *
from django.urls import path

urlpatterns = [
    path('',home)   ,
    path('blog/',blog),
    path('blog/<slug>',view),
    path('add_blog/',admin),
    path('delete/<slug>/',delete),
    path('edit/<slug>/',edit),
]
