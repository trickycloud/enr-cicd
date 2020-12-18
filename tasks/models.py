from django.db import models
from EmpApp.models import EmployeeProfile, ManagerProfile, CustomUser
from project.models import Project
from datetime import datetime
# Create your models here.


class Task(models.Model):
    by = models.ForeignKey(CustomUser, related_name="manager", on_delete=models.SET_NULL, null=True, blank=True)
    by_des = models.CharField(default="Project Owner", max_length=100)
    employee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_detail = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, null=True)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.task_detail

class Update(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    update = models.CharField(max_length=300)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.update



class TimeSheet(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null = True)
    task  = models.ForeignKey(Task, on_delete=models.CASCADE)
    subTask = models.CharField(max_length=300)
    timeSpend = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Employee Id: "+str(self.employee.user.employee_id)
