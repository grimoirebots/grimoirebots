"""grimoirebots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', get_schema_view(
        title="Grimoirebots",
        description="Run GrimoireLab in the cloud!",
        version="0.1.0"
    ), name='openapi-schema'),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls'), name='orders'),
    path('reports/', include('reports.urls'), name='reports'),
]
