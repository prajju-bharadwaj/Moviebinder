"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from moviebinder.views import home, signup, signin, project, new_project, project_overview, all_scripts, script, add_script, edit_script
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('signup/', signup),
    path('signin/', signin),
    path('myprojects/', project),
    path('newproject/', new_project),
    path('myprojects/<int:project_id>/', project_overview),
    path('allscripts/', all_scripts),
    path('addscript/', add_script),
    path('editscript/<int:script_id>/', edit_script),
    path('script/<int:script_id>/', script),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
