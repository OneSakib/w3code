from django.db import models
from MainApp.models import Comments, TutCommon, HOST_NAME
from django.urls import reverse_lazy


class CProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'CProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:cprojectsdetail", kwargs={"slug": self.slug})}'


class CPlusProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'CPlusProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:cplusprojectsdetail", kwargs={"slug": self.slug})}'


class PythonProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'PythonProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:pythonprojectsdetail", kwargs={"slug": self.slug})}'


class JavaProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:javaprojectsdetail", kwargs={"slug": self.slug})}'


class KotlinProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'KotlinProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:kotlinprojectsdetail", kwargs={"slug": self.slug})}'


class RProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'RProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:rprojectsdetail", kwargs={"slug": self.slug})}'


class CSharpProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'CSharpProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:csharpprojectsdetail", kwargs={"slug": self.slug})}'


class SwiftProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'SwiftProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:swiftprojectsdetail", kwargs={"slug": self.slug})}'


class JavaScriptProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaScriptProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:javascriptprojectsdetail", kwargs={"slug": self.slug})}'


class AndroidProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'AndroidProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:androidprojectsdetail", kwargs={"slug": self.slug})}'


class PHPProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'PHPProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:phpprojectsdetail", kwargs={"slug": self.slug})}'


class DotNetProjects(TutCommon):
    class Meta:
        verbose_name_plural = 'DotNetProjects'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Projects:dotnetprojectsdetail", kwargs={"slug": self.slug})}'
