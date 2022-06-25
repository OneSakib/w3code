from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class CProgramme_Sitemap(CommonSitemap):
    def items(self):
        return CProgramme.objects.all()


class CPlusProgramme_Sitemap(CommonSitemap):
    def items(self):
        return CPlusProgramme.objects.all()


class PythonProgramme_Sitemap(CommonSitemap):
    def items(self):
        return PythonProgramme.objects.all()


class JavaProgramme_Sitemap(CommonSitemap):
    def items(self):
        return JavaProgramme.objects.all()


class KotlinProgramme_Sitemap(CommonSitemap):
    def items(self):
        return KotlinProgramme.objects.all()


class RProgramme_Sitemap(CommonSitemap):
    def items(self):
        return RProgramme.objects.all()


class CSharpProgramme_Sitemap(CommonSitemap):
    def items(self):
        return CSharpProgramme.objects.all()


class SwiftProgramme_Sitemap(CommonSitemap):
    def items(self):
        return SwiftProgramme.objects.all()


class JavaScriptProgramme_Sitemap(CommonSitemap):
    def items(self):
        return JavaScriptProgramme.objects.all()


class PHPProgramme_Sitemap(CommonSitemap):
    def items(self):
        return PHPProgramme.objects.all()


class DotNetProgramme_Sitemap(CommonSitemap):
    def items(self):
        return DotNetProgramme.objects.all()


Pro_sitemap = {
    'CProgramme_Sitemap': CProgramme_Sitemap,
    'CPlusProgramme_Sitemap': CPlusProgramme_Sitemap,
    'PythonProgramme_Sitemap': PythonProgramme_Sitemap,
    'JavaProgramme_Sitemap': JavaProgramme_Sitemap,
    'KotlinProgramme_Sitemap': KotlinProgramme_Sitemap,
    'RProgramme_Sitemap': RProgramme_Sitemap,
    'CSharpProgramme_Sitemap': CSharpProgramme_Sitemap,
    'SwiftProgramme_Sitemap': SwiftProgramme_Sitemap,
    'JavaScriptProgramme_Sitemap': JavaScriptProgramme_Sitemap,
    'PHPProgramme_Sitemap': PHPProgramme_Sitemap,
    'DotNetProgramme_Sitemap': DotNetProgramme_Sitemap
}
