from django.urls import path

from . import views

urlpatterns = [
    path('', views.PatientCreateView.as_view(), name='index'),
]