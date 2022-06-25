from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class Jquery_Sitemap(CommonSitemap):
    def items(self):
        return Jquery.objects.all()


class Angularjs_Sitemap(CommonSitemap):
    def items(self):
        return Angularjs.objects.all()


class Nodejs_Sitemap(CommonSitemap):
    def items(self):
        return Nodejs.objects.all()


class Expressjs_Sitemap(CommonSitemap):
    def items(self):
        return Expressjs.objects.all()


class Reactjs_Sitemap(CommonSitemap):
    def items(self):
        return Reactjs.objects.all()


class TypeScripts_Sitemap(CommonSitemap):
    def items(self):
        return TypeScripts.objects.all()


class VUEjs_Sitemap(CommonSitemap):
    def items(self):
        return VUEjs.objects.all()


JS_sitemap = {
    'Jquery_Sitemap': Jquery_Sitemap,
    'Angularjs_Sitemap': Angularjs_Sitemap,
    'Nodejs_Sitemap': Nodejs_Sitemap,
    'Expressjs_Sitemap': Expressjs_Sitemap,
    'Reactjs_Sitemap': Reactjs_Sitemap,
    'TypeScripts_Sitemap': TypeScripts_Sitemap,
    'VUEjs_Sitemap': VUEjs_Sitemap
}
