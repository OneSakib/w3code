from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy
from Programmes import models as progmodel
from Projects import models as projmodel


# Create your models here.
# Parent
class CLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CLanguage Parent'

    def get_child(self):
        return CLanguage.objects.all()


class CplusLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CplusLanguage Parent'

    def get_child(self):
        return CplusLanguage.objects.all()


class PythonLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PythonLanguage Parent'

    def get_child(self):
        return PythonLanguage.objects.all()


class JavaLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaLanguage Parent'

    def get_child(self):
        return JavaLanguage.objects.all()


class AndroidLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'AndroidLanguage Parent'

    def get_child(self):
        return AndroidLanguage.objects.all()


class KotlinLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'KotlinLanguage Parent'

    def get_child(self):
        return KotlinLanguage.objects.all()


class RLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'RLanguage Parent'

    def get_child(self):
        return RLanguage.objects.all()


class CsharpLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CsharpLanguage Parent'

    def get_child(self):
        return CsharpLanguage.objects.all()


class SwiftLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SwiftLanguage Parent'

    def get_child(self):
        return SwiftLanguage.objects.all()


class JavaScriptLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaScriptLanguage Parent'

    def get_child(self):
        return JavaScriptLanguage.objects.all()


class PHPLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PHPLanguage Parent'

    def get_child(self):
        return PHPLanguage.objects.all()


class DotNetLanguageParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DotNetLanguage Parent'

    def get_child(self):
        return DotNetLanguage.objects.all()


# Child
# Programming Language
class CLanguage(TutCommon):
    parent = models.ForeignKey(CLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:cdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CProgramme.objects.all()

    def projects(self):
        return projmodel.CProjects.objects.all()


class CplusLanguage(TutCommon):
    parent = models.ForeignKey(CplusLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CplusLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:cplusdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CPlusProgramme.objects.all()

    def projects(self):
        return projmodel.CPlusProjects.objects.all()


class PythonLanguage(TutCommon):
    parent = models.ForeignKey(PythonLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PythonLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:pythondetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.PythonProgramme.objects.all()

    def projects(self):
        return projmodel.PythonProjects.objects.all()


class JavaLanguage(TutCommon):
    parent = models.ForeignKey(JavaLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:javadetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.JavaProgramme.objects.all()

    def projects(self):
        return projmodel.JavaProjects.objects.all()


class AndroidLanguage(TutCommon):
    parent = models.ForeignKey(AndroidLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'AndroidLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:androiddetail", kwargs={"slug": self.slug})}'

    def projects(self):
        return projmodel.AndroidProjects.objects.all()


class KotlinLanguage(TutCommon):
    parent = models.ForeignKey(KotlinLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'KotlinLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:kotlindetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.KotlinProgramme.objects.all()

    def projects(self):
        return projmodel.KotlinProjects.objects.all()


class RLanguage(TutCommon):
    parent = models.ForeignKey(RLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'RLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:rdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.RProgramme.objects.all()

    def projects(self):
        return projmodel.RProjects.objects.all()


class CsharpLanguage(TutCommon):
    parent = models.ForeignKey(CsharpLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CsharpLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:csharpdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.CSharpProgramme.objects.all()

    def projects(self):
        return projmodel.CSharpProjects.objects.all()


class SwiftLanguage(TutCommon):
    parent = models.ForeignKey(SwiftLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SwiftLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:swiftdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.SwiftProgramme.objects.all()

    def projects(self):
        return projmodel.SwiftProjects.objects.all()


class JavaScriptLanguage(TutCommon):
    parent = models.ForeignKey(JavaScriptLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaScriptLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:javascriptdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.JavaScriptProgramme.objects.all()

    def projects(self):
        return projmodel.JavaScriptProjects.objects.all()


class PHPLanguage(TutCommon):
    parent = models.ForeignKey(PHPLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PHPLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:phpdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.PHPProgramme.objects.all()

    def projects(self):
        return projmodel.PHPProjects.objects.all()


class DotNetLanguage(TutCommon):
    parent = models.ForeignKey(DotNetLanguageParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DotNetLanguage'

    def get_absolute_url(self):
        return f'{reverse_lazy("Programming:dotnetdetail", kwargs={"slug": self.slug})}'

    def programmes(self):
        return progmodel.DotNetProgramme.objects.all()

    def projects(self):
        return projmodel.DotNetProjects.objects.all()


# Like Counter
class CLanguageLike(LikeCommon):
    post = models.ForeignKey(CLanguage, on_delete=models.CASCADE)


class CplusLanguageLike(LikeCommon):
    post = models.ForeignKey(CplusLanguage, on_delete=models.CASCADE)


class PythonLanguageLike(LikeCommon):
    post = models.ForeignKey(PythonLanguage, on_delete=models.CASCADE)


class JavaLanguageLike(LikeCommon):
    post = models.ForeignKey(JavaLanguage, on_delete=models.CASCADE)


class AndroidLanguageLike(LikeCommon):
    post = models.ForeignKey(AndroidLanguage, on_delete=models.CASCADE)


class KotlinLanguageLike(LikeCommon):
    post = models.ForeignKey(KotlinLanguage, on_delete=models.CASCADE)


class RLanguageLike(LikeCommon):
    post = models.ForeignKey(RLanguage, on_delete=models.CASCADE)


class CsharpLanguageLike(LikeCommon):
    post = models.ForeignKey(CsharpLanguage, on_delete=models.CASCADE)


class SwiftLanguageLike(LikeCommon):
    post = models.ForeignKey(SwiftLanguage, on_delete=models.CASCADE)


class JavaScriptLanguageLike(LikeCommon):
    post = models.ForeignKey(JavaScriptLanguage, on_delete=models.CASCADE)


class PHPLanguageLike(LikeCommon):
    post = models.ForeignKey(PHPLanguage, on_delete=models.CASCADE)


class DotNetLanguageLike(LikeCommon):
    post = models.ForeignKey(DotNetLanguage, on_delete=models.CASCADE)
