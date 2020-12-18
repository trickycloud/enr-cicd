from django.contrib import admin
from django.urls import path
from . import views


app_name="EmpApp"

urlpatterns = [
    path('',views.index,name='index'),
    path('accounts/login/',views.login_view,name='login'),
    path('accounts/logout/',views.logout_view,name='logout'),
    path('accounts/edit',views.edit,name='edit'),
    path('accounts/edit/step1',views.step,name='step'),
    path('accounts/edit/<str:msg>',views.edit_msg,name='edit_profile'),
    path('accounts/profile',views.profile,name='employee_profile')
]
