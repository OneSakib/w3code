from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class MSExcel_Sitemap(CommonSitemap):
    def items(self):
        return MSExcel.objects.all()


class MSWord_Sitemap(CommonSitemap):
    def items(self):
        return MSWord.objects.all()


class MSPowerpoint_Sitemap(CommonSitemap):
    def items(self):
        return MSPowerpoint.objects.all()


class MSOneNote_Sitemap(CommonSitemap):
    def items(self):
        return MSOneNote.objects.all()


MS_sitemap = {
    'MSExcel_Sitemap': MSExcel_Sitemap,
    'MSWord_Sitemap': MSWord_Sitemap,
    'MSPowerpoint_Sitemap': MSPowerpoint_Sitemap,
    'MSOneNote_Sitemap': MSOneNote_Sitemap
}
