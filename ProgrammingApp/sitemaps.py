from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class CLanguage_Sitemap(CommonSitemap):
    def items(self):
        return CLanguage.objects.all()


class CplusLanguage_Sitemap(CommonSitemap):
    def items(self):
        return CplusLanguage.objects.all()


class PythonLanguage_Sitemap(CommonSitemap):
    def items(self):
        return PythonLanguage.objects.all()


class JavaLanguage_Sitemap(CommonSitemap):
    def items(self):
        return JavaLanguage.objects.all()


class AndroidLanguage_Sitemap(CommonSitemap):
    def items(self):
        return AndroidLanguage.objects.all()


class KotlinLanguage_Sitemap(CommonSitemap):
    def items(self):
        return KotlinLanguage.objects.all()


class RLanguage_Sitemap(CommonSitemap):
    def items(self):
        return RLanguage.objects.all()


class CsharpLanguage_Sitemap(CommonSitemap):
    def items(self):
        return CsharpLanguage.objects.all()


class SwiftLanguage_Sitemap(CommonSitemap):
    def items(self):
        return SwiftLanguage.objects.all()


class JavaScriptLanguage_Sitemap(CommonSitemap):
    def items(self):
        return JavaScriptLanguage.objects.all()


class PHPLanguage_Sitemap(CommonSitemap):
    def items(self):
        return PHPLanguage.objects.all()


class DotNetLanguage_Sitemap(CommonSitemap):
    def items(self):
        return DotNetLanguage.objects.all()


Prog_sitemap = {
    'CLanguage_Sitemap': CLanguage_Sitemap,
    'CplusLanguage_Sitemap': CplusLanguage_Sitemap,
    'PythonLanguage_Sitemap': PythonLanguage_Sitemap,
    'JavaLanguage_Sitemap': JavaLanguage_Sitemap,
    'AndroidLanguage_Sitemap': AndroidLanguage_Sitemap,
    'KotlinLanguage_Sitemap': KotlinLanguage_Sitemap,
    ' RLanguage_Sitemap': RLanguage_Sitemap,
    'CsharpLanguage_Sitemap ': CsharpLanguage_Sitemap,
    'SwiftLanguage_Sitemap ': SwiftLanguage_Sitemap,
    'JavaScriptLanguage_Sitemap ': JavaScriptLanguage_Sitemap,
    ' PHPLanguage_Sitemap': PHPLanguage_Sitemap,
    ' DotNetLanguage_Sitemap': DotNetLanguage_Sitemap,
}
