from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class HTMLs_Sitemap(CommonSitemap):
    def items(self):
        return HTMLs.objects.all()


class CSSs_Sitemap(CommonSitemap):
    def items(self):
        return CSSs.objects.all()


class Laravels_Sitemap(CommonSitemap):
    def items(self):
        return Laravels.objects.all()


class Wordpress_Sitemap(CommonSitemap):
    def items(self):
        return Wordpress.objects.all()


class JSONs_Sitemap(CommonSitemap):
    def items(self):
        return JSONs.objects.all()


class Ajaxs_Sitemap(CommonSitemap):
    def items(self):
        return Ajaxs.objects.all()


class Bootstraps_Sitemap(CommonSitemap):
    def items(self):
        return Bootstraps.objects.all()


W_sitemap = {
    'HTMLs_Sitemap': HTMLs_Sitemap,
    'CSSs_Sitemap': CSSs_Sitemap,
    'Laravels_Sitemap': Laravels_Sitemap,
    'Wordpress_Sitemap': Wordpress_Sitemap,
    'JSONs_Sitemap': JSONs_Sitemap,
    'Ajaxs_Sitemap': Ajaxs_Sitemap,
    'Bootstraps_Sitemap': Bootstraps_Sitemap,
}
