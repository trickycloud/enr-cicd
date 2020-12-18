from django.shortcuts import render, get_object_or_404
from tasks.models import Task, Update
from .models import Project, Team_member, Requirement, Documentation
from EmpApp.models import EmployeeProfile
# Create your views here.
def indi_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    tms = Team_member.objects.filter(project=project)
    emps = EmployeeProfile.objects.all().exclude(role="MANAGER")
    tasks = Task.objects.filter(project=project)
    updates = Update.objects.filter(task__in=tasks)
    reqs = Requirement.objects.filter(project=project)
    docs = Documentation.objects.filter(project=project)
    projects = Project.objects.all()
    context = {
        'project':project,
        'tms':tms,
        'tasks':tasks,
        'reqs':reqs,
        'docs':docs,
        'updates':updates
    }
    if project.lead == request.user:
        return render(request, 'employee/project_lead.html', context)
    if request.user.is_manager:
        return render(request, 'manager/project.html', context)
    return render(request, 'employee/project.html', context)
