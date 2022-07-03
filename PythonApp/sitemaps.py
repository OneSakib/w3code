from django.contrib.sitemaps import Sitemap
from .models import *
from MainApp.sitemaps import CommonSitemap


class Django_Sitemap(CommonSitemap):
    def items(self):
        return Django.objects.all()


class Flask_Sitemap(CommonSitemap):
    def items(self):
        return Flask.objects.all()


class RestApi_Sitemap(CommonSitemap):
    def items(self):
        return RestApi.objects.all()


class MachineLearning_Sitemap(CommonSitemap):
    def items(self):
        return MachineLearning.objects.all()


class Numpys_Sitemap(CommonSitemap):
    def items(self):
        return Numpys.objects.all()


class Tkinters_Sitemap(CommonSitemap):
    def items(self):
        return Tkinters.objects.all()


class Pytorchs_Sitemap(CommonSitemap):
    def items(self):
        return Pytorchs.objects.all()


class Pygames_Sitemap(CommonSitemap):
    def items(self):
        return Pygames.objects.all()


class Scipys_Sitemap(CommonSitemap):
    def items(self):
        return Scipys.objects.all()


class Pandass_Sitemap(CommonSitemap):
    def items(self):
        return Pandass.objects.all()


class OpenCVs_Sitemap(CommonSitemap):
    def items(self):
        return OpenCVs.objects.all()


class Matplotlibs_Sitemap(CommonSitemap):
    def items(self):
        return Matplotlibs.objects.all()


class Seleniums_Sitemap(CommonSitemap):
    def items(self):
        return Seleniums.objects.all()


class Kivys_Sitemap(CommonSitemap):
    def items(self):
        return Kivys.objects.all()


class Jupyters_Sitemap(CommonSitemap):
    def items(self):
        return Jupyters.objects.all()


class DataScience_Sitemap(CommonSitemap):
    def items(self):
        return DataScience.objects.all()


class DeepLearning_Sitemap(CommonSitemap):
    def items(self):
        return DeepLearning.objects.all()


class Pillows_Sitemap(CommonSitemap):
    def items(self):
        return Pillows.objects.all()


class Tensorflows_Sitemap(CommonSitemap):
    def items(self):
        return Tensorflows.objects.all()


class DSPython_Sitemap(CommonSitemap):
    def items(self):
        return DSPython.objects.all()


PY_sitemap = {
    'Django_Sitemap': Django_Sitemap,
    'RestApi_Sitemap': RestApi_Sitemap,
    'Flask_Sitemap': Flask_Sitemap,
    'MachineLearning_Sitemap': MachineLearning_Sitemap,
    'Numpys_Sitemap': Numpys_Sitemap,
    'Tkinters_Sitemap': Tkinters_Sitemap,
    'Pytorchs_Sitemap': Pytorchs_Sitemap,
    'Pygames_Sitemap ': Pygames_Sitemap,
    'Scipys_Sitemap ': Scipys_Sitemap,
    'Pandass_Sitemap ': Pandass_Sitemap,
    'OpenCVs_Sitemap': OpenCVs_Sitemap,
    'Matplotlibs_Sitemap': Matplotlibs_Sitemap,
    'Seleniums_Sitemap': Seleniums_Sitemap,
    'Kivys_Sitemap': Kivys_Sitemap,
    'Jupyters_Sitemap': Jupyters_Sitemap,
    'DataScience_Sitemap ': DataScience_Sitemap,
    'DeepLearning_Sitemap ': DeepLearning_Sitemap,
    'Pillows_Sitemap': Pillows_Sitemap,
    'Tensorflows_Sitemap': Tensorflows_Sitemap,
    'DSPython_Sitemap': DSPython_Sitemap,
}
