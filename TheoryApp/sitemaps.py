from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class DBMS_Sitemap(CommonSitemap):
    def items(self):
        return DBMS.objects.all()


class DAA_Sitemap(CommonSitemap):
    def items(self):
        return DAA.objects.all()


class OperatingSystem_Sitemap(CommonSitemap):
    def items(self):
        return OperatingSystem.objects.all()


class ComputerNetwork_Sitemap(CommonSitemap):
    def items(self):
        return ComputerNetwork.objects.all()


class CompilerDesign_Sitemap(CommonSitemap):
    def items(self):
        return CompilerDesign.objects.all()


class DiscreteMathematics_Sitemap(CommonSitemap):
    def items(self):
        return DiscreteMathematics.objects.all()


class SoftwareEngineering_Sitemap(CommonSitemap):
    def items(self):
        return SoftwareEngineering.objects.all()


class CyberSecurity_Sitemap(CommonSitemap):
    def items(self):
        return CyberSecurity.objects.all()


class DataMining_Sitemap(CommonSitemap):
    def items(self):
        return DataMining.objects.all()


class ArtificialIntelligence_Sitemap(CommonSitemap):
    def items(self):
        return ArtificialIntelligence.objects.all()


class Automata_Sitemap(CommonSitemap):
    def items(self):
        return Automata.objects.all()


class ComputerGraphics_Sitemap(CommonSitemap):
    def items(self):
        return ComputerGraphics.objects.all()


class WebApi_Sitemap(CommonSitemap):
    def items(self):
        return WebApi.objects.all()


TH_sitemap = {
    'DBMS_Sitemap': DBMS_Sitemap,
    'DAA_Sitemap': DAA_Sitemap,
    'OperatingSystem_Sitemap': OperatingSystem_Sitemap,
    'ComputerNetwork_Sitemap': ComputerNetwork_Sitemap,
    'CompilerDesign_Sitemap': CompilerDesign_Sitemap,
    'DiscreteMathematics_Sitemap': DiscreteMathematics_Sitemap,
    'SoftwareEngineering_Sitemap ': SoftwareEngineering_Sitemap,
    'CyberSecurity_Sitemap ': CyberSecurity_Sitemap,
    'DataMining_Sitemap ': DataMining_Sitemap,
    ' ArtificialIntelligence_Sitemap': ArtificialIntelligence_Sitemap,
    'Automata_Sitemap ': Automata_Sitemap,
    'ComputerGraphics_Sitemap ': ComputerGraphics_Sitemap,
    ' WebApi_Sitemap': WebApi_Sitemap
}
