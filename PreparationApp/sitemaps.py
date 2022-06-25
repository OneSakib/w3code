from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class Aptitude_Sitemap(CommonSitemap):
    def items(self):
        return Aptitude.objects.all()


class Reasoning_Sitemap(CommonSitemap):
    def items(self):
        return Reasoning.objects.all()


class VerbalAbility_Sitemap(CommonSitemap):
    def items(self):
        return VerbalAbility.objects.all()


class InterviewQuestion_Sitemap(CommonSitemap):
    def items(self):
        return InterviewQuestion.objects.all()


class CompanyQuestion_Sitemap(CommonSitemap):
    def items(self):
        return CompanyQuestion.objects.all()


Pre_sitemap = {
    'Aptitude_Sitemap': Aptitude_Sitemap,
    'Reasoning_Sitemap': Reasoning_Sitemap,
    'VerbalAbility_Sitemap': VerbalAbility_Sitemap,
    'InterviewQuestion_Sitemap': InterviewQuestion_Sitemap,
    'CompanyQuestion_Sitemap': CompanyQuestion_Sitemap
}
