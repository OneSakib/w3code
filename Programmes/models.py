from django.db import models
from MainApp.models import TutCommon, LikeCommon, TutCommonParent
from django.urls import reverse_lazy


# Create your models here.
# Parent
class CProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CProgramme Parent'

    def get_child(self):
        return CProgramme.objects.all()


class CPlusProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CPlusProgramme Parent'

    def get_child(self):
        return CPlusProgramme.objects.all()


class PythonProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PythonProgramme Parent'

    def get_child(self):
        return PythonProgramme.objects.all()


class JavaProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaProgramme Parent'

    def get_child(self):
        return JavaProgramme.objects.all()


class KotlinProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'KotlinProgramme Parent'

    def get_child(self):
        return KotlinProgramme.objects.all()


class RProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'RProgramme Parent'

    def get_child(self):
        return RProgramme.objects.all()


class CSharpProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CSharpProgramme Parent'

    def get_child(self):
        return CSharpProgramme.objects.all()


class SwiftProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SwiftProgramme Parent'

    def get_child(self):
        return SwiftProgramme.objects.all()


class JavaScriptProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaScriptProgramme Parent'

    def get_child(self):
        return JavaScriptProgramme.objects.all()


class PHPProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PHPProgramme Parent'

    def get_child(self):
        return PHPProgramme.objects.all()


class DotNetProgrammeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DotNetProgramme Parent'

    def get_child(self):
        return DotNetProgramme.objects.all()


# Child
class CProgramme(TutCommon):
    parent = models.ForeignKey(CProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:cprogrammedetail", kwargs={"slug": self.slug})}'


class CPlusProgramme(TutCommon):
    parent = models.ForeignKey(CPlusProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CPlusProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:cplusprogrammedetail", kwargs={"slug": self.slug})}'


class PythonProgramme(TutCommon):
    parent = models.ForeignKey(PythonProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PythonProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:pythonprogrammedetail", kwargs={"slug": self.slug})}'


class JavaProgramme(TutCommon):
    parent = models.ForeignKey(JavaProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:javaprogrammedetail", kwargs={"slug": self.slug})}'


class KotlinProgramme(TutCommon):
    parent = models.ForeignKey(KotlinProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'KotlinProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:kotlinprogrammedetail", kwargs={"slug": self.slug})}'


class RProgramme(TutCommon):
    parent = models.ForeignKey(RProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'RProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:rprogrammedetail", kwargs={"slug": self.slug})}'


class CSharpProgramme(TutCommon):
    parent = models.ForeignKey(CSharpProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CSharpProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:csharpprogrammedetail", kwargs={"slug": self.slug})}'


class SwiftProgramme(TutCommon):
    parent = models.ForeignKey(SwiftProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SwiftProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:swiftprogrammedetail", kwargs={"slug": self.slug})}'


class JavaScriptProgramme(TutCommon):
    parent = models.ForeignKey(JavaScriptProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaScriptProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:javascriptprogrammedetail", kwargs={"slug": self.slug})}'


class PHPProgramme(TutCommon):
    parent = models.ForeignKey(PHPProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PHPProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:phpprogrammedetail", kwargs={"slug": self.slug})}'


class DotNetProgramme(TutCommon):
    parent = models.ForeignKey(DotNetProgrammeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DotNetProgramme'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programme:dotnetprogrammedetail", kwargs={"slug": self.slug})}'


# Like Counter
class CProgrammeLike(LikeCommon):
    post = models.ForeignKey(CProgramme, on_delete=models.CASCADE)


class CPlusProgrammeLike(LikeCommon):
    post = models.ForeignKey(CPlusProgramme, on_delete=models.CASCADE)


class PythonProgrammeLike(LikeCommon):
    post = models.ForeignKey(PythonProgramme, on_delete=models.CASCADE)


class JavaProgrammeLike(LikeCommon):
    post = models.ForeignKey(JavaProgramme, on_delete=models.CASCADE)


class KotlinProgrammeLike(LikeCommon):
    post = models.ForeignKey(KotlinProgramme, on_delete=models.CASCADE)


class RProgrammeLike(LikeCommon):
    post = models.ForeignKey(RProgramme, on_delete=models.CASCADE)


class CSharpProgrammeLike(LikeCommon):
    post = models.ForeignKey(CSharpProgramme, on_delete=models.CASCADE)


class SwiftProgrammeLike(LikeCommon):
    post = models.ForeignKey(SwiftProgramme, on_delete=models.CASCADE)


class JavaScriptProgrammeLike(LikeCommon):
    post = models.ForeignKey(JavaScriptProgramme, on_delete=models.CASCADE)


class PHPProgrammeLike(LikeCommon):
    post = models.ForeignKey(PHPProgramme, on_delete=models.CASCADE)


class DotNetProgrammeLike(LikeCommon):
    post = models.ForeignKey(DotNetProgramme, on_delete=models.CASCADE)
