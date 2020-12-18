from django.shortcuts import render, redirect
from EmpApp.models import EmployeeProfile, SessionLogs, AdminMessage
import datetime
from project.models import Project, Team_member
from tasks.models import Task

def employee_dash(request):
    try:
        profile = EmployeeProfile.objects.get(user=request.user)
        if not profile.done:
            return redirect("EmpApp:edit")
    except:
        profile = False
    if not profile:
        return redirect("EmpApp:edit_profile", msg="newuser_redirect")

    enddate = datetime.date.today() + datetime.timedelta(days=1)
    startdate = enddate - datetime.timedelta(days=6)
    sessions = SessionLogs.objects.filter(user=request.user, login_time__range=[startdate, enddate]).order_by('login_time')
    time_logged_in = []
    print(sessions)
    # first = sessions[:1].login_time.date()
    # print(first)
    seconds = 0
    day_hour = []
    dicts_lis = []
    try:
        k = sessions[0].login_time.strftime("%d/%m/%Y")
    except:
        pass
    for session in sessions:
        if k == session.login_time.strftime("%d/%m/%Y"):
            try:
                z = session.logout_time-session.login_time
                seconds+= z.total_seconds()
                print(seconds, z)
            except:
                day_hour.append([k, seconds/3600])
                dicts_lis.append({'label':k, 'y':seconds/3600})
                k = session.login_time.strftime("%d/%m/%Y")
                seconds = 0
            continue
        day_hour.append([k, seconds/3600])
        dicts_lis.append({'label':k, 'y':seconds/3600})
        k = session.login_time.strftime("%d/%m/%Y")
        seconds = 0
    involved_in = Team_member.objects.filter(member=profile)
    my_projects = []
    for i in involved_in:
        mp = []
        project = Project.objects.get(id=i.project.id)
        mp.append(project)
        mp.append(Task.objects.filter(employee=request.user, project=project))
        my_projects.append(mp)
    print(day_hour)


    return render(request, 'employee/employeedash.html', {'sessions':day_hour[::-1], 'session2':dicts_lis, 'projects': my_projects})



def admin_message(request):
    if request.user.is_authenticated:
        messages = AdminMessage.objects.filter(to=request.user)
        context = {
            'messages':messages,
        }
        print(context)
        for i in messages:
            i.seen = True
            i.save()
        return render(request, 'employee/from_admin.html', context)
