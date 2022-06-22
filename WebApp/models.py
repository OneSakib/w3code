from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# web Technology
class HTMLs(TutCommon):
    class Meta:
        verbose_name_plural = 'HTMLs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:htmldetail", kwargs={"slug": self.slug})}'


class CSSs(TutCommon):
    class Meta:
        verbose_name_plural = 'CSSs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:cssdetail", kwargs={"slug": self.slug})}'


class Laravels(TutCommon):
    class Meta:
        verbose_name_plural = 'Laravels'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:laraveldetail", kwargs={"slug": self.slug})}'


class Wordpress(TutCommon):
    class Meta:
        verbose_name_plural = 'Wordpress'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:wordpressdetail", kwargs={"slug": self.slug})}'


class JSONs(TutCommon):
    class Meta:
        verbose_name_plural = 'JSONs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:jsondetail", kwargs={"slug": self.slug})}'


class Ajaxs(TutCommon):
    class Meta:
        verbose_name_plural = 'Ajaxs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:ajaxdetail", kwargs={"slug": self.slug})}'


class Bootstraps(TutCommon):
    class Meta:
        verbose_name_plural = 'Bootstraps'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Web:bootstrapdetail", kwargs={"slug": self.slug})}'


# Comments
class HTMLsComments(Comments):
    post = models.ForeignKey(HTMLs, on_delete=models.CASCADE, related_name='HTMLsComments')

    class Meta:
        verbose_name_plural = 'HTMLsComments'


class CSSsComments(Comments):
    post = models.ForeignKey(CSSs, on_delete=models.CASCADE, related_name='CSSsComments')

    class Meta:
        verbose_name_plural = 'CSSsComments'


class LaravelsComments(Comments):
    post = models.ForeignKey(Laravels, on_delete=models.CASCADE, related_name='LaravelsComments')

    class Meta:
        verbose_name_plural = 'LaravelsComments'


class WordpressComments(Comments):
    post = models.ForeignKey(Wordpress, on_delete=models.CASCADE, related_name='WordpressComments')

    class Meta:
        verbose_name_plural = 'WordpressComments'


class JSONsComments(Comments):
    post = models.ForeignKey(JSONs, on_delete=models.CASCADE, related_name='JSONsComments')

    class Meta:
        verbose_name_plural = 'JSONsComments'


class AjaxsComments(Comments):
    post = models.ForeignKey(Ajaxs, on_delete=models.CASCADE, related_name='AjaxsComments')

    class Meta:
        verbose_name_plural = 'AjaxsComments'


class BootstrapsComments(Comments):
    post = models.ForeignKey(Bootstraps, on_delete=models.CASCADE, related_name='BootstrapsComments')

    class Meta:
        verbose_name_plural = 'BootstrapsComments'
