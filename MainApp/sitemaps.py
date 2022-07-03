from django.contrib.sitemaps import Sitemap
from .models import *


class CommonSitemap(Sitemap):
    change_freq = "weekly"
    priority = 1

    def lastmod(self, obj):
        return obj.timestamp


class Static_sitemap(Sitemap):
    changefreq = 'yearly'
    priority = 1

    def items(self):
        return ['w3c:index']

    def location(self, item):
        return reverse_lazy(item)


class Blogs_Sitemap(CommonSitemap):
    def items(self):
        return Blogs.objects.all()


M_sitemap = {
    'Static_sitemap': Static_sitemap,
    'Blogs_Sitemap': Blogs_Sitemap,
}
