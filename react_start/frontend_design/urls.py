from django.urls import path
from . import views

urlpatterns = [
    path('design/', views.design, name="design"),
    path('react/', views.react_template, name="react-template"),
]