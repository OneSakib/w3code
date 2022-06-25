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
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:cdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CProgramme.objects.all()

    def projects(self):
        return projmodel.CProjects.objects.all()


class CplusLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CplusLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:cplusdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CPlusProgramme.objects.all()

    def projects(self):
        return projmodel.CPlusProjects.objects.all()


class PythonLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'PythonLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:pythondetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.PythonProgramme.objects.all()

    def projects(self):
        return projmodel.PythonProjects.objects.all()


class JavaLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:javadetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.JavaProgramme.objects.all()

    def projects(self):
        return projmodel.JavaProjects.objects.all()


class AndroidLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'AndroidLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:androiddetail", kwargs={"slug": self.slug})}'

    def projects(self):
        return projmodel.AndroidProjects.objects.all()


class KotlinLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'KotlinLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:kotlindetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.KotlinProgramme.objects.all()

    def projects(self):
        return projmodel.KotlinProjects.objects.all()


class RLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'RLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:rdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.RProgramme.objects.all()

    def projects(self):
        return projmodel.RProjects.objects.all()


class CsharpLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CsharpLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:csharpdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CSharpProgramme.objects.all()

    def projects(self):
        return projmodel.CSharpProjects.objects.all()


class SwiftLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'SwiftLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:swiftdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.SwiftProgramme.objects.all()

    def projects(self):
        return projmodel.SwiftProjects.objects.all()


class JavaScriptLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaScriptLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:javascriptdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.JavaScriptProgramme.objects.all()

    def projects(self):
        return projmodel.JavaScriptProjects.objects.all()


class PHPLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'PHPLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:phpdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.PHPProgramme.objects.all()

    def projects(self):
        return projmodel.PHPProjects.objects.all()


class DotNetLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'DotNetLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:dotnetdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.DotNetProgramme.objects.all()

    def projects(self):
        return projmodel.DotNetProjects.objects.all()


# Comments
class CLanguageComments(Comments):
    post = models.ForeignKey(CLanguage, on_delete=models.CASCADE, related_name='CLanguageComments')

    class Meta:
        verbose_name_plural = 'CLanguageComments'


class CplusLanguageComments(Comments):
    post = models.ForeignKey(CplusLanguage, on_delete=models.CASCADE, related_name='CplusLanguageComments')

    class Meta:
        verbose_name_plural = 'CplusLanguageComments'


class PythonLanguageComments(Comments):
    post = models.ForeignKey(PythonLanguage, on_delete=models.CASCADE, related_name='PythonLanguageComments')

    class Meta:
        verbose_name_plural = 'PythonLanguageComments'


class JavaLanguageComments(Comments):
    post = models.ForeignKey(JavaLanguage, on_delete=models.CASCADE, related_name='JavaLanguageComments')

    class Meta:
        verbose_name_plural = 'JavaLanguageComments'


class AndroidLanguageComments(Comments):
    post = models.ForeignKey(AndroidLanguage, on_delete=models.CASCADE, related_name='AndroidLanguageComments')

    class Meta:
        verbose_name_plural = 'AndroidLanguageComments'


class KotlinLanguageComments(Comments):
    post = models.ForeignKey(KotlinLanguage, on_delete=models.CASCADE, related_name='KotlinLanguageComments')

    class Meta:
        verbose_name_plural = 'KotlinLanguageComments'


class RLanguageComments(Comments):
    post = models.ForeignKey(RLanguage, on_delete=models.CASCADE, related_name='RLanguageComments')

    class Meta:
        verbose_name_plural = 'RLanguageComments'


class CsharpLanguageComments(Comments):
    post = models.ForeignKey(CsharpLanguage, on_delete=models.CASCADE, related_name='CsharpLanguageComments')

    class Meta:
        verbose_name_plural = 'CsharpLanguageComments'


class SwiftLanguageComments(Comments):
    post = models.ForeignKey(SwiftLanguage, on_delete=models.CASCADE, related_name='SwiftLanguageComments')

    class Meta:
        verbose_name_plural = 'SwiftLanguageComments'


class JavaScriptLanguageComments(Comments):
    post = models.ForeignKey(JavaScriptLanguage, on_delete=models.CASCADE, related_name='JavaScriptLanguageComments')

    class Meta:
        verbose_name_plural = 'JavaScriptLanguageComments'


class PHPLanguageComments(Comments):
    post = models.ForeignKey(PHPLanguage, on_delete=models.CASCADE, related_name='PHPLanguageComments')

    class Meta:
        verbose_name_plural = 'PHPLanguageComments'


class DotNetLanguageComments(Comments):
    post = models.ForeignKey(DotNetLanguage, on_delete=models.CASCADE, related_name='DotNetLanguageComments')

    class Meta:
        verbose_name_plural = 'DotNetLanguageComments'
