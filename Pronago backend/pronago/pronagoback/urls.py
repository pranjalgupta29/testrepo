from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='pronago-home'),
    path('clothing/', views.categories, name='pronago-categories')

    ]
