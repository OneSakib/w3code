from django.contrib.sitemaps import Sitemap
from .models import *


class CommonSitemap(Sitemap):
    change_freq = "weekly"
    priority = 0.7

    def lastmod(self, obj):
        return obj.timestamp


class Blogs_Sitemap(CommonSitemap):
    def items(self):
        return Blogs.objects.all()


M_sitemap = {
    'Blogs_Sitemap': Blogs_Sitemap
}
