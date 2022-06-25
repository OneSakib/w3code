from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class CProjects_Sitemap(CommonSitemap):
    def items(self):
        return CProjects.objects.all()


class CPlusProjects_Sitemap(CommonSitemap):
    def items(self):
        return CPlusProjects.objects.all()


class PythonProjects_Sitemap(CommonSitemap):
    def items(self):
        return PythonProjects.objects.all()


class JavaProjects_Sitemap(CommonSitemap):
    def items(self):
        return JavaProjects.objects.all()


class KotlinProjects_Sitemap(CommonSitemap):
    def items(self):
        return KotlinProjects.objects.all()


class RProjects_Sitemap(CommonSitemap):
    def items(self):
        return RProjects.objects.all()


class CSharpProjects_Sitemap(CommonSitemap):
    def items(self):
        return CSharpProjects.objects.all()


class SwiftProjects_Sitemap(CommonSitemap):
    def items(self):
        return SwiftProjects.objects.all()


class JavaScriptProjects_Sitemap(CommonSitemap):
    def items(self):
        return JavaScriptProjects.objects.all()


class AndroidProjects_Sitemap(CommonSitemap):
    def items(self):
        return AndroidProjects.objects.all()


class PHPProjects_Sitemap(CommonSitemap):
    def items(self):
        return PHPProjects.objects.all()


class DotNetProjects_Sitemap(CommonSitemap):
    def items(self):
        return DotNetProjects.objects.all()


Proj_sitemap = {
    'CProjects_Sitemap': CProjects_Sitemap,
    'CPlusProjects_Sitemap': CPlusProjects_Sitemap,
    'PythonProjects_Sitemap': PythonProjects_Sitemap,
    'JavaProjects_Sitemap': JavaProjects_Sitemap,
    'KotlinProjects_Sitemap': KotlinProjects_Sitemap,
    'RProjects_Sitemap': RProjects_Sitemap,
    ' CSharpProjects_Sitemap': CSharpProjects_Sitemap,
    'SwiftProjects_Sitemap ': SwiftProjects_Sitemap,
    'JavaScriptProjects_Sitemap ': JavaScriptProjects_Sitemap,
    ' AndroidProjects_Sitemap': AndroidProjects_Sitemap,
    'PHPProjects_Sitemap ': PHPProjects_Sitemap,
    'DotNetProjects_Sitemap ': DotNetProjects_Sitemap,
}
