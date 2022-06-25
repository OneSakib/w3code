from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class Docker_Sitemap(CommonSitemap):
    def items(self):
        return Docker.objects.all()


class Gits_Sitemap(CommonSitemap):
    def items(self):
        return Gits.objects.all()


class Githubs_Sitemap(CommonSitemap):
    def items(self):
        return Githubs.objects.all()


VC_sitemap = {
    'Docker_Sitemap': Docker_Sitemap,
    'Gits_Sitemap': Gits_Sitemap,
    'Githubs_Sitemap': Githubs_Sitemap,

}
