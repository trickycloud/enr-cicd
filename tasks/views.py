from django.shortcuts import render, redirect
from .models import Task, Update, TimeSheet
from .forms import TimeSheetForm
from project.models import Project
from EmpApp.models import CustomUser, EmployeeProfile
from django.forms import inlineformset_factory



def addTask(request):
    details = request.POST['details']
    employee = CustomUser.objects.get(employee_id=request.POST['employee'])
    project = Project.objects.get(id=request.POST['project'])
    try:
        ManagerProfile.objects.get(user=request.user)
        by_des = request.user.name+" (Project Owner)"
    except:
        by_des = request.user.name+" (Team Lead)"
    Task.objects.create(task_detail=details, employee=employee, by=request.user, by_des=by_des, project=project)
    return redirect('project:project_slug_detail', project.slug)




def updateTask(request):
    update = request.POST['update']
    print(request.POST)
    task = Task.objects.get(id=request.POST['task'])
    project = Project.objects.get(id=request.POST['project'])
    Update.objects.create(update=update, task=task)
    return redirect('project:project_slug_detail', project.slug)


def timesheet(request):
    user_p = EmployeeProfile.objects.get(user=request.user)
    time_sheet_formset = inlineformset_factory(EmployeeProfile, TimeSheet, TimeSheetForm, extra=1, can_delete=True)
    if request.method=="POST":
        form = time_sheet_formset(request.POST, instance=user_p)
        if form.is_valid():
            form.save()
        return redirect("EmpApp:logout")
