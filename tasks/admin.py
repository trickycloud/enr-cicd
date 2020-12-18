from django.contrib import admin


from .models import Task, Update, TimeSheet





admin.site.register(Task)
admin.site.register(TimeSheet)
admin.site.register(Update)
