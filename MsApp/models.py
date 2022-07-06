from django.db import models
from MainApp.models import TutCommon, LikeCommon, TutCommonParent
from django.urls import reverse_lazy


# Create your models here.

# Parent
class MSExcelParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MSExcel Parent'

    def get_child(self):
        return MSExcel.objects.all()


class MSWordParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MSWord Parent'

    def get_child(self):
        return MSWord.objects.all()


class MSPowerpointParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MSPowerpoint Parent'

    def get_child(self):
        return MSPowerpoint.objects.all()


class MSOneNoteParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MSOneNote Parent'

    def get_child(self):
        return MSOneNote.objects.all()


# Child
# MS Office
class MSExcel(TutCommon):
    parent = models.ForeignKey(MSExcelParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MSExcel'

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:msexceldetail", kwargs={"slug": self.slug})}'


class MSWord(TutCommon):
    parent = models.ForeignKey(MSWordParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MSWord'

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:msworddetail", kwargs={"slug": self.slug})}'


class MSPowerpoint(TutCommon):
    parent = models.ForeignKey(MSPowerpointParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MSPowerpoint'

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:mspowerpointdetail", kwargs={"slug": self.slug})}'


class MSOneNote(TutCommon):
    parent = models.ForeignKey(MSOneNoteParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MSOneNote'

    def get_absolute_url(self):
        return f'{reverse_lazy("MS:msonenotedetail", kwargs={"slug": self.slug})}'


# Like Counter
class MSExcelLike(LikeCommon):
    post = models.ForeignKey(MSExcel, on_delete=models.CASCADE)


class MSWordLike(LikeCommon):
    post = models.ForeignKey(MSWord, on_delete=models.CASCADE)


class MSPowerpointLike(LikeCommon):
    post = models.ForeignKey(MSPowerpoint, on_delete=models.CASCADE)


class MSOneNoteLike(LikeCommon):
    post = models.ForeignKey(MSOneNote, on_delete=models.CASCADE)
