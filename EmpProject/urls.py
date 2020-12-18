"""EmpProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    # path('nested_admin/', include('nested_admin.urls')),
    path('',include('EmpApp.urls')),
    path('project/',include('project.urls')),
    path('admin/', admin.site.urls),
    path('employee/',include('employee.urls')),
    path('tasks/',include('tasks.urls')),
    path('manager/',include('manager.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
