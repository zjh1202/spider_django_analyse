"""analysis_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include
from analysis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('analysis.url')),
    path('base/', views.base),
    path('python/', views.python_technology),
    path('java/', views.java_technology),
    path('data/', views.data_technology),
    path('Android/', views.Android_technology),
    path('algorithm/', views.algorithm_technology),
    path('min_average_wages/', views.min_average_wages),
    path('max_average_wages/', views.max_average_wages),
]
