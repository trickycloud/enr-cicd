from django.contrib import admin
from django.urls import path
from . import views


app_name="manager"

urlpatterns = [
    path('dashboard',views.manager_dash,name = 'dashboard'),
    path('projects',views.my_projects,name = 'my_projects'),
    path('messages/admin/',views.admin_message,name='admin_msg'),
]
