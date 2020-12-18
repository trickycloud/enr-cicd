from django.contrib import admin
from django.urls import path
from . import views


app_name="employee"

urlpatterns = [
    path('messages/admin/',views.admin_message,name='admin_msg'),
    path('dashboard',views.employee_dash,name = 'dashboard'),
]
