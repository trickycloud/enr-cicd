from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import SessionLogs, BroadcastMessage, AdminMessage
import datetime


@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    session_Logs = SessionLogs.objects.filter(session_key=request.session.session_key, user=user.employee_id)[:1]
    if not session_Logs:
        session_Log = SessionLogs(login_time=datetime.datetime.now(),session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
        session_Log.save()



@receiver(user_logged_out)
def post_logout(sender, user, request, **kwargs):
    session_Logs = SessionLogs.objects.filter(session_key=request.session.session_key, user=user.employee_id, host=request.META['HTTP_HOST'])
    session_Logs.filter(logout_time__isnull=True).update(logout_time=datetime.datetime.now())
    if not session_Logs:
        session_Log = SessionLogs(logout_time=datetime.datetime.now(), session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
        session_Log.save()

@receiver(m2m_changed, sender=BroadcastMessage.to.through)
def save_profile(sender, instance, **kwargs):
    print(instance.to.all(), "signal Initiated")
    for i in instance.to.all():
        AdminMessage.objects.create(to=i, message=instance.message, )
