from django.contrib import admin
from .models import Project, Team_member, Requirement, Documentation


class TeamMemberInline(admin.TabularInline):
    model = Team_member
    extra = 1

class DocumentationInline(admin.TabularInline):
    model = Documentation
    extra = 1

class RequirementFilesInline(admin.TabularInline):
    model = Requirement
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = ( RequirementFilesInline, TeamMemberInline, DocumentationInline )


admin.site.register(Project, ProjectAdmin)
