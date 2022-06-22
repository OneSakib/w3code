"""w3code URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls', namespace='w3c')),
    path('programming/', include('ProgrammingApp.urls', namespace='Programming')),
    path('preparation/', include('PreparationApp.urls', namespace='Preparation')),
    path('theory/', include('TheoryApp.urls', namespace='Theory')),
    path('db/', include('DatabaseApp.urls', namespace='Database')),
    path('python/', include('PythonApp.urls', namespace='Python')),
    path('java/', include('JavaApp.urls', namespace='Java')),
    path('javascript/', include('JavaScriptApp.urls', namespace='Javascript')),
    path('web/', include('WebApp.urls', namespace='Web')),
    path('ms/', include('MsApp.urls', namespace='MS')),
    path('vc/', include('VCApp.urls', namespace='VC')),
]
