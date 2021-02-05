"""form1_project URL Configuration

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
from movie_app import views as m
# import ftplib

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/',views.show),
    # path('form1/',views.studentreg),
    # path('form2/',v1.empregview),
    
    #Movie app urls
    path('',m.display),
    path('addmovie/',m.add_new_movie),
    path('viewlist/',m.display_list),
    path('about/',m.about_us),

    #deployment URL
    # url(r'^ftpdeploy/', include('ftp_deploy.urls')),
    # url(r'^ftpdeploy/', include('ftp_deploy.server.urls')),
]
