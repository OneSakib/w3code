from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.

# JavaScript
class Jquery(TutCommon):
    class Meta:
        verbose_name_plural = 'Jquery'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:jquerydetail", kwargs={"slug": self.slug})}'


class Angularjs(TutCommon):
    class Meta:
        verbose_name_plural = 'Angularjs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:angulardetail", kwargs={"slug": self.slug})}'


class Nodejs(TutCommon):
    class Meta:
        verbose_name_plural = 'Nodejs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:nodejsdetail", kwargs={"slug": self.slug})}'


class Expressjs(TutCommon):
    class Meta:
        verbose_name_plural = 'Expressjs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:expressjsdetail", kwargs={"slug": self.slug})}'


class Reactjs(TutCommon):
    class Meta:
        verbose_name_plural = 'Reactjs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:reactjsdetail", kwargs={"slug": self.slug})}'


class TypeScripts(TutCommon):
    class Meta:
        verbose_name_plural = 'TypeScripts'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:typescriptdetail", kwargs={"slug": self.slug})}'


class VUEjs(TutCommon):
    class Meta:
        verbose_name_plural = 'VUEjs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:vuejsdetail", kwargs={"slug": self.slug})}'


