from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# MS Office
class MSExcel(TutCommon):
    class Meta:
        verbose_name_plural = 'MSExcel'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("MS:msexceldetail", kwargs={"slug": self.slug})}'


class MSWord(TutCommon):
    class Meta:
        verbose_name_plural = 'MSWord'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("MS:msworddetail", kwargs={"slug": self.slug})}'


class MSPowerpoint(TutCommon):
    class Meta:
        verbose_name_plural = 'MSPowerpoint'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("MS:mspowerpointdetail", kwargs={"slug": self.slug})}'


class MSOneNote(TutCommon):
    class Meta:
        verbose_name_plural = 'MSOneNote'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("MS:msonenotedetail", kwargs={"slug": self.slug})}'


# Comments

class MSWordComments(Comments):
    post = models.ForeignKey(MSWord, on_delete=models.CASCADE, related_name='MSWordComments')

    class Meta:
        verbose_name_plural = 'MSWordComments'


class MSExcelComments(Comments):
    post = models.ForeignKey(MSExcel, on_delete=models.CASCADE, related_name='MSExcelComments')

    class Meta:
        verbose_name_plural = 'MSExcelComments'


class MSPowerpointComments(Comments):
    post = models.ForeignKey(MSPowerpoint, on_delete=models.CASCADE, related_name='MSPowerpointComments')

    class Meta:
        verbose_name_plural = 'MSPowerpointComments'


class MSOneNoteComments(Comments):
    post = models.ForeignKey(MSOneNote, on_delete=models.CASCADE, related_name='MSOneNoteComments')

    class Meta:
        verbose_name_plural = 'MSOneNoteComments'
