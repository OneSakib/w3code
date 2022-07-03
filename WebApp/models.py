from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# web Technology
class HTMLs(TutCommon):
    class Meta:
        verbose_name_plural = 'HTMLs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:htmldetail", kwargs={"slug": self.slug})}'


class CSSs(TutCommon):
    class Meta:
        verbose_name_plural = 'CSSs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:cssdetail", kwargs={"slug": self.slug})}'


class Laravels(TutCommon):
    class Meta:
        verbose_name_plural = 'Laravels'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:laraveldetail", kwargs={"slug": self.slug})}'


class Wordpress(TutCommon):
    class Meta:
        verbose_name_plural = 'Wordpress'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:wordpressdetail", kwargs={"slug": self.slug})}'


class JSONs(TutCommon):
    class Meta:
        verbose_name_plural = 'JSONs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:jsondetail", kwargs={"slug": self.slug})}'


class Ajaxs(TutCommon):
    class Meta:
        verbose_name_plural = 'Ajaxs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:ajaxdetail", kwargs={"slug": self.slug})}'


class Bootstraps(TutCommon):
    class Meta:
        verbose_name_plural = 'Bootstraps'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:bootstrapdetail", kwargs={"slug": self.slug})}'

