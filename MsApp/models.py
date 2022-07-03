from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# MS Office
class MSExcel(TutCommon):
    class Meta:
        verbose_name_plural = 'MSExcel'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:msexceldetail", kwargs={"slug": self.slug})}'


class MSWord(TutCommon):
    class Meta:
        verbose_name_plural = 'MSWord'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:msworddetail", kwargs={"slug": self.slug})}'


class MSPowerpoint(TutCommon):
    class Meta:
        verbose_name_plural = 'MSPowerpoint'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:mspowerpointdetail", kwargs={"slug": self.slug})}'


class MSOneNote(TutCommon):
    class Meta:
        verbose_name_plural = 'MSOneNote'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:msonenotedetail", kwargs={"slug": self.slug})}'

