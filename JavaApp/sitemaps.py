from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class Servlets_Sitemap(CommonSitemap):
    def items(self):
        return Servlets.objects.all()


class JSPs_Sitemap(CommonSitemap):
    def items(self):
        return JSPs.objects.all()


class SpringBoot_Sitemap(CommonSitemap):
    def items(self):
        return SpringBoot.objects.all()


class SpringFramework_Sitemap(CommonSitemap):
    def items(self):
        return SpringFramework.objects.all()


class Hibernates_Sitemap(CommonSitemap):
    def items(self):
        return Hibernates.objects.all()


class JavaSwings_Sitemap(CommonSitemap):
    def items(self):
        return JavaSwings.objects.all()


class JavaFXs_Sitemap(CommonSitemap):
    def items(self):
        return JavaFXs.objects.all()


class JavaAWT_Sitemap(CommonSitemap):
    def items(self):
        return JavaAWT.objects.all()


class Collections_Sitemap(CommonSitemap):
    def items(self):
        return Collections.objects.all()


class JavaDate_Sitemap(CommonSitemap):
    def items(self):
        return JavaDate.objects.all()


class JavaIO_Sitemap(CommonSitemap):
    def items(self):
        return JavaIO.objects.all()


J_sitemap = {
    'Servlets_Sitemap': Servlets_Sitemap,
    'JSPs_Sitemap': JSPs_Sitemap,
    'SpringBoot_Sitemap': SpringBoot_Sitemap,
    'SpringFramework_Sitemap': SpringFramework_Sitemap,
    'Hibernates_Sitemap': Hibernates_Sitemap,
    'JavaSwings_Sitemap': JavaSwings_Sitemap,
    'JavaFXs_Sitemap ': JavaFXs_Sitemap,
    ' JavaAWT_Sitemap': JavaAWT_Sitemap,
    ' Collections_Sitemap': Collections_Sitemap,
    ' JavaDate_Sitemap': JavaDate_Sitemap,
    ' JavaIO_Sitemap': JavaIO_Sitemap
}
