from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Python Tut
class Django(TutCommon):
    class Meta:
        verbose_name_plural = 'Django'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:djangodetail", kwargs={"slug": self.slug})}'


class RestApi(TutCommon):
    class Meta:
        verbose_name_plural = 'RestApi'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:restapidetail", kwargs={"slug": self.slug})}'


class Flask(TutCommon):
    class Meta:
        verbose_name_plural = 'Flask'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:flaskdetail", kwargs={"slug": self.slug})}'


class MachineLearning(TutCommon):
    class Meta:
        verbose_name_plural = 'MachineLearning'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:machinelearningdetail", kwargs={"slug": self.slug})}'


class Numpys(TutCommon):
    class Meta:
        verbose_name_plural = 'Numpys'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:numpydetail", kwargs={"slug": self.slug})}'


class Tkinters(TutCommon):
    class Meta:
        verbose_name_plural = 'Tkinters'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:tkinterdetail", kwargs={"slug": self.slug})}'


class Pytorchs(TutCommon):
    class Meta:
        verbose_name_plural = 'Pytorchs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pytorchdetail", kwargs={"slug": self.slug})}'


class Pygames(TutCommon):
    class Meta:
        verbose_name_plural = 'Pygames'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pygamedetail", kwargs={"slug": self.slug})}'


class Scipys(TutCommon):
    class Meta:
        verbose_name_plural = 'Scipys'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:scipydetail", kwargs={"slug": self.slug})}'


class Pandass(TutCommon):
    class Meta:
        verbose_name_plural = 'Pandass'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pandasdetail", kwargs={"slug": self.slug})}'


class OpenCVs(TutCommon):
    class Meta:
        verbose_name_plural = 'OpenCVs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:opencvdetail", kwargs={"slug": self.slug})}'


class Matplotlibs(TutCommon):
    class Meta:
        verbose_name_plural = 'Matplotlibs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:matplotlibdetail", kwargs={"slug": self.slug})}'


class Seleniums(TutCommon):
    class Meta:
        verbose_name_plural = 'Seleniums'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:seleniumdetail", kwargs={"slug": self.slug})}'


class Kivys(TutCommon):
    class Meta:
        verbose_name_plural = 'Kivys'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:kivydetail", kwargs={"slug": self.slug})}'


class Jupyters(TutCommon):
    class Meta:
        verbose_name_plural = 'Jupyters'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:jupyterdetail", kwargs={"slug": self.slug})}'


class DataScience(TutCommon):
    class Meta:
        verbose_name_plural = 'DataScience'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:datasciencedetail", kwargs={"slug": self.slug})}'


class DeepLearning(TutCommon):
    class Meta:
        verbose_name_plural = 'DeepLearning'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:deeplearningdetail", kwargs={"slug": self.slug})}'


class Pillows(TutCommon):
    class Meta:
        verbose_name_plural = 'Pillows'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pillowdetail", kwargs={"slug": self.slug})}'


class Tensorflows(TutCommon):
    class Meta:
        verbose_name_plural = 'Tensorflows'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:tensorflowdetail", kwargs={"slug": self.slug})}'


class DSPython(TutCommon):
    class Meta:
        verbose_name_plural = 'DSPython'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:dspythondetail", kwargs={"slug": self.slug})}'

