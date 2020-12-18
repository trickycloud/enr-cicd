from django.test import TestCase
from .models import AdminMessage, EmployeeProfile
from tasks.forms import TimeSheetForm
from tasks.models import TimeSheet
from django.forms import inlineformset_factory








def admin_message_count(request):
    try:
        count = AdminMessage.objects.filter(to=request.user).filter(seen=False).count()
    except:
        count = 0
    return {'count': count}


def time_sheet_form(request):
    form = TimeSheetForm()
    time_sheet_formset = inlineformset_factory(EmployeeProfile, TimeSheet, TimeSheetForm, extra=1, can_delete=True)

    return {'time_sheet_form':form, 'time_sheet_formset':time_sheet_formset}
# Create your tests here.
