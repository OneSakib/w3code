from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.

# JavaScript
class Jquery(TutCommon):
    class Meta:
        verbose_name_plural = 'Jquery'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:jquerydetail", kwargs={"slug": self.slug})}'


class Angularjs(TutCommon):
    class Meta:
        verbose_name_plural = 'Angularjs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:angulardetail", kwargs={"slug": self.slug})}'


class Nodejs(TutCommon):
    class Meta:
        verbose_name_plural = 'Nodejs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:nodejsdetail", kwargs={"slug": self.slug})}'


class Expressjs(TutCommon):
    class Meta:
        verbose_name_plural = 'Expressjs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:expressjsdetail", kwargs={"slug": self.slug})}'


class Reactjs(TutCommon):
    class Meta:
        verbose_name_plural = 'Reactjs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:reactjsdetail", kwargs={"slug": self.slug})}'


class TypeScripts(TutCommon):
    class Meta:
        verbose_name_plural = 'TypeScripts'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:typescriptdetail", kwargs={"slug": self.slug})}'


class VUEjs(TutCommon):
    class Meta:
        verbose_name_plural = 'VUEjs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("JavaScript:vuejsdetail", kwargs={"slug": self.slug})}'


# Comments
class JqueryComments(Comments):
    post = models.ForeignKey(Jquery, on_delete=models.CASCADE, related_name='JqueryComments')

    class Meta:
        verbose_name_plural = 'JqueryComments'


class AngularjsComments(Comments):
    post = models.ForeignKey(Angularjs, on_delete=models.CASCADE, related_name='AngularjsComments')

    class Meta:
        verbose_name_plural = 'AngularjsComments'


class NodejsComments(Comments):
    post = models.ForeignKey(Nodejs, on_delete=models.CASCADE, related_name='NodejsComments')

    class Meta:
        verbose_name_plural = 'NodejsComments'


class ExpressjsComments(Comments):
    post = models.ForeignKey(Expressjs, on_delete=models.CASCADE, related_name='ExpressjsComments')

    class Meta:
        verbose_name_plural = 'ExpressjsComments'


class ReactjsComments(Comments):
    post = models.ForeignKey(Reactjs, on_delete=models.CASCADE, related_name='ReactjsComments')

    class Meta:
        verbose_name_plural = 'ReactjsComments'


class TypeScriptsComments(Comments):
    post = models.ForeignKey(TypeScripts, on_delete=models.CASCADE, related_name='TypeScriptsComments')

    class Meta:
        verbose_name_plural = 'TypeScriptsComments'


class VUEjsComments(Comments):
    post = models.ForeignKey(VUEjs, on_delete=models.CASCADE, related_name='VUEjsComments')

    class Meta:
        verbose_name_plural = 'VUEjsComments'
