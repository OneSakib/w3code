from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class DigitalOcean_Sitemap(CommonSitemap):
    def items(self):
        return DigitalOcean.objects.all()


class MSAzure_Sitemap(CommonSitemap):
    def items(self):
        return MSAzure.objects.all()


class AWS_Sitemap(CommonSitemap):
    def items(self):
        return AWS.objects.all()


class PythonAnywhere_Sitemap(CommonSitemap):
    def items(self):
        return PythonAnywhere.objects.all()


class HerokuApp_Sitemap(CommonSitemap):
    def items(self):
        return HerokuApp.objects.all()


class GithubHost_Sitemap(CommonSitemap):
    def items(self):
        return GithubHost.objects.all()


class BlueHost_Sitemap(CommonSitemap):
    def items(self):
        return BlueHost.objects.all()


class HostGator_Sitemap(CommonSitemap):
    def items(self):
        return HostGator.objects.all()


class InMotionHosting_Sitemap(CommonSitemap):
    def items(self):
        return InMotionHosting.objects.all()


class A2Hosting_Sitemap(CommonSitemap):
    def items(self):
        return A2Hosting.objects.all()


class GreenGeeks_Sitemap(CommonSitemap):
    def items(self):
        return GreenGeeks.objects.all()


class Hostinger_Sitemap(CommonSitemap):
    def items(self):
        return Hostinger.objects.all()


class GoDaddy_Sitemap(CommonSitemap):
    def items(self):
        return GoDaddy.objects.all()


Host_sitemap = {
    'DigitalOcean_Sitemap': DigitalOcean_Sitemap,
    'MSAzure_Sitemap': MSAzure_Sitemap,
    'AWS_Sitemap': AWS_Sitemap,
    'PythonAnywhere_Sitemap': PythonAnywhere_Sitemap,
    'HerokuApp_Sitemap': HerokuApp_Sitemap,
    'GithubHost_Sitemap': GithubHost_Sitemap,
    'BlueHost_Sitemap ': BlueHost_Sitemap,
    'HostGator_Sitemap': HostGator_Sitemap,
    ' InMotionHosting_Sitemap': InMotionHosting_Sitemap,
    'A2Hosting_Sitemap ': A2Hosting_Sitemap,
    ' GreenGeeks_Sitemap': GreenGeeks_Sitemap,
    'Hostinger_Sitemap ': Hostinger_Sitemap,
    ' GoDaddy_Sitemap': GoDaddy_Sitemap,
}
