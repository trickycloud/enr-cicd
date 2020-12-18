from django.contrib import admin
from django.urls import path
from . import views


app_name="project"

urlpatterns = [
    path('<str:slug>',views.indi_project,name='project_slug_detail'),
]
