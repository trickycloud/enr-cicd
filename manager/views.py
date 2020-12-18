from django.shortcuts import render, redirect
from EmpApp.models import EmployeeProfile, SessionLogs, ManagerProfile, AdminMessage
from EmpApp.decorators import is_manager
from project.models import Project

@is_manager(redirect_field_name="/")
def manager_dash(request):
    try:
        print(request.user)
        profile = EmployeeProfile.objects.get(user=request.user)
        print("profile", profile)
        if not profile.done:
            return redirect("EmpApp:edit")
    except:
        profile = False
    if not profile:
        return redirect("EmpApp:edit_profile", msg="newuser_redirect")

    mprofile = ManagerProfile.objects.get(employee=profile)
    my_projects = Project.objects.filter(manager=mprofile, completed=False)
    return render(request, 'manager/managerdash.html', {'projects':my_projects[:3]})


@is_manager(redirect_field_name="/")
def my_projects(request):
    pass






@is_manager(redirect_field_name="/")
def admin_message(request):
    messages = AdminMessage.objects.filter(to=request.user)
    context = {
        'messages':messages,
    }
    print(context)
    return render(request, 'manager/from_admin.html', context)
