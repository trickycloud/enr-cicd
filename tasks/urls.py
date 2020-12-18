from django.urls import path,include
from . import views



app_name="tasks"
urlpatterns = [

    path('add', views.addTask, name="addTask"),
    path('timesheet', views.timesheet, name="timesheet"),
    path('update', views.updateTask, name="updateTask"),

]
