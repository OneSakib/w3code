from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.
# Java

class Servlets(TutCommon):
    class Meta:
        verbose_name_plural = 'Servlets'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:servletdetail", kwargs={"slug": self.slug})}'


class JSPs(TutCommon):
    class Meta:
        verbose_name_plural = 'JSPs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:jspdetail", kwargs={"slug": self.slug})}'


class SpringBoot(TutCommon):
    class Meta:
        verbose_name_plural = 'SpringBoot'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:springbootdetail", kwargs={"slug": self.slug})}'


class SpringFramework(TutCommon):
    class Meta:
        verbose_name_plural = 'SpringFramework'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:springframeworkdetail", kwargs={"slug": self.slug})}'


class Hibernates(TutCommon):
    class Meta:
        verbose_name_plural = 'Hibernates'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:hibernatedetail", kwargs={"slug": self.slug})}'


class JavaSwings(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaSwings'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:javaswingdetail", kwargs={"slug": self.slug})}'


class JavaFXs(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaFXs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:javafxdetail", kwargs={"slug": self.slug})}'


class JavaAWT(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaAWT'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:javaawtdetail", kwargs={"slug": self.slug})}'


class Collections(TutCommon):
    class Meta:
        verbose_name_plural = 'Collections'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:javacollectionsdetail", kwargs={"slug": self.slug})}'


class JavaDate(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaDate'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:javadatedetail", kwargs={"slug": self.slug})}'


class JavaIO(TutCommon):
    class Meta:
        verbose_name_plural = 'JavaIO'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Java:javaiodetail", kwargs={"slug": self.slug})}'


# Comments

class ServletsComments(Comments):
    post = models.ForeignKey(Servlets, on_delete=models.CASCADE, related_name='ServletsComments')

    class Meta:
        verbose_name_plural = 'ServletsComments'


class JSPsComments(Comments):
    post = models.ForeignKey(JSPs, on_delete=models.CASCADE, related_name='JSPsComments')

    class Meta:
        verbose_name_plural = 'JSPsComments'


class SpringBootComments(Comments):
    post = models.ForeignKey(SpringBoot, on_delete=models.CASCADE, related_name='SpringBootComments')

    class Meta:
        verbose_name_plural = 'SpringBootComments'


class SpringFrameworkComments(Comments):
    post = models.ForeignKey(SpringFramework, on_delete=models.CASCADE, related_name='SpringFrameworkComments')

    class Meta:
        verbose_name_plural = 'SpringFrameworkComments'


class HibernatesComments(Comments):
    post = models.ForeignKey(Hibernates, on_delete=models.CASCADE, related_name='HibernatesComments')

    class Meta:
        verbose_name_plural = 'HibernatesComments'


class JavaSwingsComments(Comments):
    post = models.ForeignKey(JavaSwings, on_delete=models.CASCADE, related_name='JavaSwingsComments')

    class Meta:
        verbose_name_plural = 'JavaSwingsComments'


class JavaFXsComments(Comments):
    post = models.ForeignKey(JavaFXs, on_delete=models.CASCADE, related_name='JavaFXsComments')

    class Meta:
        verbose_name_plural = 'JavaFXsComments'


class JavaAWTComments(Comments):
    post = models.ForeignKey(JavaAWT, on_delete=models.CASCADE, related_name='JavaAWTComments')

    class Meta:
        verbose_name_plural = 'JavaAWTComments'


class CollectionsComments(Comments):
    post = models.ForeignKey(Collections, on_delete=models.CASCADE, related_name='CollectionsComments')

    class Meta:
        verbose_name_plural = 'CollectionsComments'


class JavaDateComments(Comments):
    post = models.ForeignKey(JavaDate, on_delete=models.CASCADE, related_name='JavaDateComments')

    class Meta:
        verbose_name_plural = 'JavaDateComments'


class JavaIOComments(Comments):
    post = models.ForeignKey(JavaIO, on_delete=models.CASCADE, related_name='JavaIOComments')

    class Meta:
        verbose_name_plural = 'JavaIOComments'
