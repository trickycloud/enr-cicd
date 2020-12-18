from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


DEPARTMENT = (
    ('HR','Human Resource Manager'),
    ('ACCOUNTS','Account Manager'),
    ('PROJECTS','Project Manager'),
)

EMPLOYEE_ROLE = (
    ('BACKEND','Backend Developer'),
    ('FRONTEND','Frontend Developer'),
    ('GRAPHICS','Graphics Designer'),
    ('WEB_DESIGN','Web Designer'),
    ('FULL_STACK','Full Stack Developer'),
    ('MARKETING','Marketing'),
    ('MANAGER', 'Manager')
)

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = "All Users"
    employee_id = models.AutoField(primary_key=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_manager = models.BooleanField(default=False)
    department = models.CharField(max_length=50, choices=DEPARTMENT, null=True, blank=True, default=None)
    is_employee = models.BooleanField(default=False)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        if self.name == None:
            return super().__str__()
        return self.name + " id: "+ str(self.employee_id)

class SessionLogs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=200, blank=False, null=False)
    host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.name



def employee_profile(instance, filename):
    return 'employee/id-{0}/{1}'.format(instance.user.employee_id, filename)

def employee_profile_certi(instance, filename):
    return 'employee/id-{0}/{1}'.format(instance.employee.user.employee_id, filename)


class EmployeeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cv = models.FileField(upload_to=employee_profile, null=True, blank=True)
    cv_approved = models.BooleanField(default=False)
    cv_defects = models.CharField(max_length=200, default=None, null=True, blank=True)
    govt_issued_id = models.FileField(upload_to=employee_profile, null=True, blank=True)
    govt_issued_id_approved = models.BooleanField(default=False)
    govt_issued_id_defects = models.CharField(max_length=200, default=None, null=True, blank=True)
    phone_no = models.IntegerField(null=True, blank=True)
    phone_approved = models.BooleanField(default=False)
    phone_defects = models.CharField(max_length=200, default=None, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    address_approved = models.BooleanField(default=False)
    address_defects = models.CharField(max_length=200, default=None, null=True, blank=True)
    role = models.CharField(choices=EMPLOYEE_ROLE, max_length=50)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.name)+" id: "+str(self.user.employee_id)



class ManagerProfile(models.Model):
    employee = models.OneToOneField(EmployeeProfile, on_delete=models.CASCADE)
    some = models.CharField(max_length=20)
    def __str__(self):
        return str(self.employee.user.name)+" id: "+str(self.employee.user.employee_id)



class Skill(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True)
    skill = models.CharField(max_length=100)
    rating = models.IntegerField()

class Certification(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    certificate = models.FileField(upload_to=employee_profile_certi)


class FuturePlan(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True)
    technology = models.CharField(max_length=100)

class Responce(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True)
    skill_development = models.BooleanField(default=False)
    suggession = models.CharField(max_length=300, blank=True)

class LiveInteraction(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.CharField(max_length=200)
    time_required = models.IntegerField()
    on = models.DateField()
    when = models.TimeField()


class ManagerRight(models.Model):
    manager = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    add_projects = models.BooleanField()
    add_employees = models.BooleanField()
    handle_payments = models.BooleanField()
    add_teammembers = models.BooleanField()


class BroadcastMessage(models.Model):
    to = models.ManyToManyField(CustomUser)
    message = models.CharField(max_length=500)


class AdminMessage(models.Model):
    to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=True, blank=True)
    seen = models.BooleanField(default=False)
