"""
URL configuration for webdog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views as core_views
from service import views as service_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.inicio, name="inicio"),
    path('quienes/', core_views.quienes, name="quienes"),
    path('guarderia/', core_views.guarderia, name="guarderia"),
    path('contactos/', core_views.contactos, name="contactos"),
    path('historia/', core_views.historia, name="historia"),
    path('servicios/', service_views.servicios, name="servicios"),
]
