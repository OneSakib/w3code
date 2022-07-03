from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.
# Java

class Servlets(TutCommon):
    class Meta:
        verbose_name_plural = 'Servlets'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:servletdetail", kwargs={"slug": self.slug})}'


class JSPs(TutCommon):
    class Meta:
        verbose_name_plural = 'JSPs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:jspdetail", kwargs={"slug": self.slug})}'


class SpringBoot(TutCommon):
    class Meta:
        verbose_name_plural = 'SpringBoot'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:springbootdetail", kwargs={"slug": self.slug})}'


class SpringFramework(TutCommon):
    class Meta:
        verbose_name_plural = 'SpringFramework'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:springframeworkdetail", kwargs={"slug": self.slug})}'


class Hibernates(TutCommon):
    class Meta:
        verbose_name_plural = 'Hibernates'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:hibernatedetail", kwargs={"slug": self.slug})}'


class JavaSwings(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaSwings'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javaswingdetail", kwargs={"slug": self.slug})}'


class JavaFXs(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaFXs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javafxdetail", kwargs={"slug": self.slug})}'


class JavaAWT(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaAWT'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javaawtdetail", kwargs={"slug": self.slug})}'


class Collections(TutCommon):
    class Meta:
        verbose_name_plural = 'Collections'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javacollectionsdetail", kwargs={"slug": self.slug})}'


class JavaDate(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaDate'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javadatedetail", kwargs={"slug": self.slug})}'


class JavaIO(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaIO'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javaiodetail", kwargs={"slug": self.slug})}'


