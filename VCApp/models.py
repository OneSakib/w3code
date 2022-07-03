from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Versioning Control
class Docker(TutCommon):
    class Meta:
        verbose_name_plural = 'Docker'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("VC:dockerdetail", kwargs={"slug": self.slug})}'


class Gits(TutCommon):
    class Meta:
        verbose_name_plural = 'Gits'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("VC:gitdetail", kwargs={"slug": self.slug})}'


class Githubs(TutCommon):
    class Meta:
        verbose_name_plural = 'Githubs'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("VC:githubdetail", kwargs={"slug": self.slug})}'

