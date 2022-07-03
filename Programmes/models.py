from django.db import models
from MainApp.models import Comments, TutCommon, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.
class CProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'CProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:cprogrammedetail", kwargs={"slug": self.slug})}'


class CPlusProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'CPlusProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:cplusprogrammedetail", kwargs={"slug": self.slug})}'


class PythonProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'PythonProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:pythonprogrammedetail", kwargs={"slug": self.slug})}'


class JavaProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:javaprogrammedetail", kwargs={"slug": self.slug})}'


class KotlinProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'KotlinProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:kotlinprogrammedetail", kwargs={"slug": self.slug})}'


class RProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'RProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:rprogrammedetail", kwargs={"slug": self.slug})}'


class CSharpProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'CSharpProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:csharpprogrammedetail", kwargs={"slug": self.slug})}'


class SwiftProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'SwiftProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:swiftprogrammedetail", kwargs={"slug": self.slug})}'


class JavaScriptProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaScriptProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:javascriptprogrammedetail", kwargs={"slug": self.slug})}'


class PHPProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'PHPProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:phpprogrammedetail", kwargs={"slug": self.slug})}'


class DotNetProgramme(TutCommon):
    class Meta:
        verbose_name_plural = 'DotNetProgramme'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:dotnetprogrammedetail", kwargs={"slug": self.slug})}'
