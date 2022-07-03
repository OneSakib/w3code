from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy
from Programmes import models as progmodel
from Projects import models as projmodel


# Create your models here.

# Programming Language
class CLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:cdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CProgramme.objects.all()

    def projects(self):
        return projmodel.CProjects.objects.all()


class CplusLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CplusLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:cplusdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CPlusProgramme.objects.all()

    def projects(self):
        return projmodel.CPlusProjects.objects.all()


class PythonLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'PythonLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:pythondetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.PythonProgramme.objects.all()

    def projects(self):
        return projmodel.PythonProjects.objects.all()


class JavaLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:javadetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.JavaProgramme.objects.all()

    def projects(self):
        return projmodel.JavaProjects.objects.all()


class AndroidLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'AndroidLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:androiddetail", kwargs={"slug": self.slug})}'

    def projects(self):
        return projmodel.AndroidProjects.objects.all()


class KotlinLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'KotlinLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:kotlindetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.KotlinProgramme.objects.all()

    def projects(self):
        return projmodel.KotlinProjects.objects.all()


class RLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'RLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:rdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.RProgramme.objects.all()

    def projects(self):
        return projmodel.RProjects.objects.all()


class CsharpLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CsharpLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:csharpdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CSharpProgramme.objects.all()

    def projects(self):
        return projmodel.CSharpProjects.objects.all()


class SwiftLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'SwiftLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:swiftdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.SwiftProgramme.objects.all()

    def projects(self):
        return projmodel.SwiftProjects.objects.all()


class JavaScriptLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaScriptLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:javascriptdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.JavaScriptProgramme.objects.all()

    def projects(self):
        return projmodel.JavaScriptProjects.objects.all()


class PHPLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'PHPLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:phpdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.PHPProgramme.objects.all()

    def projects(self):
        return projmodel.PHPProjects.objects.all()


class DotNetLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'DotNetLanguage'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:dotnetdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.DotNetProgramme.objects.all()

    def projects(self):
        return projmodel.DotNetProjects.objects.all()

