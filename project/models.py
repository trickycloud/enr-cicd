from django.db import models
from EmpApp.models import CustomUser, ManagerProfile, EmployeeProfile
from django.shortcuts import reverse
import os
from django.utils.text import slugify
import itertools



def project_requirement_directory(instance, filename):
    return 'projects/{0}/requirement_files/{1}'.format(instance.project.name, filename)

def project_documentation_directory(instance, filename):
    return 'projects/{0}/documentation_files/{1}'.format(instance.project.name, filename)

PROJECT_TYPE = (
    ('INTERNAL','Internal Project'),
    ('CLIENT','Client Project'),
)

class Project(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.DateField()
    type = models.CharField(choices=PROJECT_TYPE, max_length=100)
    manager = models.ForeignKey(ManagerProfile, null=True, on_delete=models.SET_NULL)
    lead = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    repository = models.URLField(max_length=200)
    slug = models.SlugField(max_length = 200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        # return "/project/%s" % self.slug
        return reverse('project:project_slug_detail', kwargs=kwargs)


    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.name
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Project.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

class Team_member(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(EmployeeProfile, null=True, on_delete=models.SET_NULL)


class Requirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    requirement_file = models.FileField(upload_to=project_requirement_directory)

    def filename(self):
        return os.path.basename(self.requirement_file.name)

class Documentation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to=project_documentation_directory)

    def filename(self):
        return os.path.basename(self.file.name)


# Create your models here.
