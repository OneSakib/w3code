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
from django.contrib.sitemaps.views import sitemap
from DatabaseApp.sitemaps import D_sitemap
from Exercise.sitemaps import E_sitemap
from JavaApp.sitemaps import J_sitemap
from JavaScriptApp.sitemaps import JS_sitemap
from MainApp.sitemaps import M_sitemap
from MsApp.sitemaps import MS_sitemap
from PreparationApp.sitemaps import Pre_sitemap
from ProgrammingApp.sitemaps import Prog_sitemap
from Programmes.sitemaps import Pro_sitemap
from Projects.sitemaps import Proj_sitemap
from PythonApp.sitemaps import PY_sitemap
from TheoryApp.sitemaps import TH_sitemap
from VCApp.sitemaps import VC_sitemap
from WebApp.sitemaps import W_sitemap
from HostingApp.sitemaps import Host_sitemap
from django.conf import settings
from django.conf.urls.static import static

# Admin page customization
admin.site.site_header = "W3Code.tech"
admin.site.site_title = "W3Code.tech Admin Portal"
admin.site.index_title = "W3Code.tech"

sitemaps = dict()
sitemaps.update(M_sitemap)
sitemaps.update(D_sitemap)
sitemaps.update(E_sitemap)
sitemaps.update(J_sitemap)
sitemaps.update(JS_sitemap)
sitemaps.update(MS_sitemap)
sitemaps.update(Pre_sitemap)
sitemaps.update(Pro_sitemap)
sitemaps.update(Prog_sitemap)
sitemaps.update(Proj_sitemap)
sitemaps.update(PY_sitemap)
sitemaps.update(TH_sitemap)
sitemaps.update(VC_sitemap)
sitemaps.update(W_sitemap)
sitemaps.update(Host_sitemap)

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
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
                  path('exercise/', include('Exercise.urls', namespace='Exercise')),
                  path('programme/', include('Programmes.urls', namespace='Programme')),
                  path('projects/', include('Projects.urls', namespace='Projects')),
                  path('hosting/', include('HostingApp.urls', namespace='Hosting')),
                  path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),
                  path('accounts/', include('allauth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'MainApp.views.error_404'
