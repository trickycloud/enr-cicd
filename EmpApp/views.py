from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import CustomUser, EmployeeProfile, Skill, Certification, FuturePlan, Responce, LiveInteraction
from .forms import SkillsForm, CertificationForm, FuturePlanForm, ResponceForm, LiveInteractionForm


# Main page access to everyone
def index(request):
    if request.user.is_authenticated:
        return redirect(check_user(request.user))
    return render(request,'index.html')
# Only for register user
def intro(request):
    if request.session.has_key('is_logged') :
        email = request.session['email']
        return render(request,'index.html',{'email':email})
    return redirect('index')


def check_user(user):
    if user.is_manager:
        return 'manager:dashboard'
    else:
        return 'employee:dashboard' #redirect should be returned


def login_view(request):
    if request.method =='POST':
        email = request.POST['email']
        password =request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(check_user(user))
        else:
            messages.info(request,'Invelid Credentials.')
    return render(request,'login.html')


# Only for register user
def profile(request):
    if request.user.is_authenticated:
        try:
            profile = EmployeeProfile.objects.get(user=request.user)
            if profile.phone_no==None or profile.cv=='' or profile.govt_issued_id=='' or profile.address==None:
                return redirect("EmpApp:edit")
        except:
            return redirect("EmpApp:edit")
        skills = Skill.objects.filter(employee=profile)
        template = 'employee/Employee_Profile.html'
        if request.user.is_manager:
            template = 'manager/Manager_Profile.html'
        return render(request, template, {'profile': profile, 'skills':skills})
    return render(request,'login.html')

# Only for register user
def edit(request):
    if request.user.is_authenticated:
        # skillsformset = inlineformset_factory(EmployeeProfile, Skill, SkillsForm, extra=1, can_delete=True)
        name = request.user.name
        first = False
        try:
            user_p = EmployeeProfile.objects.get(user=request.user)
        except:
            user_p = False
        if request.method == "POST":
            details = dict()
            for key in request.POST:
                if key=='name':
                    name = request.POST[key]
                elif key in ['csrfmiddlewaretoken']:
                    pass
                    continue
                elif request.POST[key] != '' and key in [f.name for f in EmployeeProfile._meta.fields]:
                    details[key] = request.POST[key]
            print(details)
            if user_p:
                EmployeeProfile.objects.filter(user=request.user).update(**details)
                user_p = EmployeeProfile.objects.get(user=request.user)
            else:
                user_p = EmployeeProfile.objects.create(user=request.user,**details)
            if not user_p.cv:
                first = True
            try:
                if request.FILES['cv'] != '':
                    user_p.cv = request.FILES['cv']
            except:
                pass
            try:
                if request.FILES['govt_issued_id'] != '':
                    user_p.govt_issued_id = request.FILES['govt_issued_id']
            except:
                pass
            user_p.save()
            CustomUser.objects.filter(employee_id=request.user.employee_id).update(name=name)
            # print(request.POST)
            # formset = skillsformset(request.POST, instance=user_p)
            # if formset.is_valid():
            #     formset.save()
            if(first):
                return redirect("EmpApp:step")
            return redirect("EmpApp:employee_profile")
        msg = None
        if(user_p.phone_no==None):
            msg = 'Tell us about yourself before you continue!'
        return render(request, 'employee/edit.html', {'user': user_p, 'name': name, 'msg':msg})
        # return render(request, 'employee/edit.html', {'user': user_p, 'name': name, 'skill_form':skillsformset, 'msg':msg})
    return redirect('/')



def step(request):
    if request.user.is_authenticated:
        user_p = EmployeeProfile.objects.get(user=request.user)
        if user_p.done:
            return redirect("employee:dashboard")
        skillsformset = inlineformset_factory(EmployeeProfile, Skill, SkillsForm, extra=1, can_delete=True)
        certificateformset = inlineformset_factory(EmployeeProfile, Certification, CertificationForm, extra=1, can_delete=True)
        futureformset = inlineformset_factory(EmployeeProfile, FuturePlan, FuturePlanForm, extra=1, can_delete=True)
        responceformset = inlineformset_factory(EmployeeProfile, Responce, ResponceForm, extra=1, can_delete=True)
        interactionformset = inlineformset_factory(EmployeeProfile, LiveInteraction, LiveInteractionForm, extra=1, can_delete=True)
        if request.method == "POST":
            formset = skillsformset(request.POST, instance=user_p)
            formset1 = certificateformset(request.POST, request.FILES, instance=user_p)
            formset2 = futureformset(request.POST, instance=user_p)
            formset4 = interactionformset(request.POST, instance=user_p)
            #
            # responce = {
            #     'skill_development':request.POST['skill_development'],
            #     'suggession':request.POST['suggession'],
            #     'employee': user_p
            # }
            #
            # Responce.objects.create(**responce)
            if formset.is_valid():
                formset.save()
            if formset1.is_valid():
                formset1.save()
            if formset2.is_valid():
                formset2.save()
            if formset4.is_valid():
                formset4.save()
            user_p.done = True
            user_p.save()
            return redirect("EmpApp:employee_profile")
        context = {
            'skill_form':skillsformset,
            'certificate_form':certificateformset,
            'future_form':futureformset,
            'responce_form':ResponceForm,
            'interaction_form':interactionformset,
        }
        return render(request, 'employee/editStep.html', context)



# Only for register user
def edit_msg(request, msg):
    if request.user.is_authenticated:
        try:
            user = EmployeeProfile.objects.get(user=request.user)
        except:
            user = None
        if request.method == "POST":
            pass
        return render(request, 'employee/edit.html', {'user': user, 'msg':'Tell us about yourself before you continue!'})
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('EmpApp:login')
