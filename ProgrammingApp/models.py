from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.

# Programming Language
class CLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:cdetail", kwargs={"slug": self.slug})}'


class CplusLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CplusLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:cplusdetail", kwargs={"slug": self.slug})}'


class PythonLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'PythonLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:pythondetail", kwargs={"slug": self.slug})}'


class JavaLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:javadetail", kwargs={"slug": self.slug})}'


class AndroidLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'AndroidLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:androiddetail", kwargs={"slug": self.slug})}'


class KotlinLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'KotlinLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:kotlindetail", kwargs={"slug": self.slug})}'


class RLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'RLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:rdetail", kwargs={"slug": self.slug})}'


class CsharpLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'CsharpLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:csharpdetail", kwargs={"slug": self.slug})}'


class SwiftLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'SwiftLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:swiftdetail", kwargs={"slug": self.slug})}'


class JavaScriptLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaScriptLanguag'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:javascriptdetail", kwargs={"slug": self.slug})}'


class PHPLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'PHPLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:phpdetail", kwargs={"slug": self.slug})}'


class DotNetLanguage(TutCommon):
    class Meta:
        verbose_name_plural = 'DotNetLanguage'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Programming:dotnetdetail", kwargs={"slug": self.slug})}'


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
    post = models.ForeignKey(JavaLanguage, on_delete=models.CASCADE, related_name='JavaScriptLanguageComments')

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
