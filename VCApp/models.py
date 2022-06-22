from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Versioning Control
class Docker(TutCommon):
    class Meta:
        verbose_name_plural = 'Docker'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("VC:dockerdetail", kwargs={"slug": self.slug})}'


class Gits(TutCommon):
    class Meta:
        verbose_name_plural = 'Gits'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("VC:gitdetail", kwargs={"slug": self.slug})}'


class Githubs(TutCommon):
    class Meta:
        verbose_name_plural = 'Githubs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("VC:githubdetail", kwargs={"slug": self.slug})}'


# comments
class DockerComments(Comments):
    post = models.ForeignKey(Docker, on_delete=models.CASCADE, related_name='DockerComments')

    class Meta:
        verbose_name_plural = 'DockerComments'


class GitsComments(Comments):
    post = models.ForeignKey(Gits, on_delete=models.CASCADE, related_name='GitsComments')

    class Meta:
        verbose_name_plural = 'GitsComments'


class GithubsComments(Comments):
    post = models.ForeignKey(Githubs, on_delete=models.CASCADE, related_name='GithubsComments')

    class Meta:
        verbose_name_plural = 'GithubsComments'
