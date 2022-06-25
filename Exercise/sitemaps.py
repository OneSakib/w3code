from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class CExercise_Sitemap(CommonSitemap):
    def items(self):
        return CExercise.objects.all()


class CPlusExercise_Sitemap(CommonSitemap):
    def items(self):
        return CPlusExercise.objects.all()


class PythonExercise_Sitemap(CommonSitemap):
    def items(self):
        return PythonExercise.objects.all()


class JavaExercise_Sitemap(CommonSitemap):
    def items(self):
        return JavaExercise.objects.all()


class KotlinExercise_Sitemap(CommonSitemap):
    def items(self):
        return KotlinExercise.objects.all()


class RExercise_Sitemap(CommonSitemap):
    def items(self):
        return RExercise.objects.all()


class CSharpExercise_Sitemap(CommonSitemap):
    def items(self):
        return CSharpExercise.objects.all()


class SwiftExercise_Sitemap(CommonSitemap):
    def items(self):
        return SwiftExercise.objects.all()


class JavaScriptExercise_Sitemap(CommonSitemap):
    def items(self):
        return JavaScriptExercise.objects.all()


class PHPExercise_Sitemap(CommonSitemap):
    def items(self):
        return PHPExercise.objects.all()


class DotNetExercise_Sitemap(CommonSitemap):
    def items(self):
        return DotNetExercise.objects.all()


E_sitemap = {
    'CExercise_Sitemap': CExercise_Sitemap,
    'CPlusExercise_Sitemap': CPlusExercise_Sitemap,
    'PythonExercise_Sitemap': PythonExercise_Sitemap,
    'JavaExercise_Sitemap': JavaExercise_Sitemap,
    'KotlinExercise_Sitemap': KotlinExercise_Sitemap,
    'RExercise_Sitemap': RExercise_Sitemap,
    ' CSharpExercise_Sitemap': CSharpExercise_Sitemap,
    'SwiftExercise_Sitemap ': SwiftExercise_Sitemap,
    ' JavaScriptExercise_Sitemap': JavaScriptExercise_Sitemap,
    'PHPExercise_Sitemap ': PHPExercise_Sitemap,
    'DotNetExercise_Sitemap ': DotNetExercise_Sitemap
}
