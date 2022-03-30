"""logon_in URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from posts.views import *
#--------------------------upload--------------------------------
from django.conf import settings
from django.conf.urls.static import static
import django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('index/',index,name='Index'),
    path('register/',sign_up,name='Register'),
    path('login/',sign_in,name='Login'),
    path('',sign_in),
    path('logout', log_out, name='Logout'),
    path('upload/',upload,name='Loadup'),
    path('upload/success/',success),
    path('listall/',list_all)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
