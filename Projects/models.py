from django.db import models
from MainApp.models import TutCommonParent, TutCommon, LikeCommon
from django.urls import reverse_lazy


# parent
# Parent
class CProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CProjects Parent'

    def get_child(self):
        return CProjects.objects.all()


class CPlusProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CPlusProjects Parent'

    def get_child(self):
        return CPlusProjects.objects.all()


class PythonProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PythonProjects Parent'

    def get_child(self):
        return PythonProjects.objects.all()


class JavaProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaProjects Parent'

    def get_child(self):
        return JavaProjects.objects.all()


class KotlinProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'KotlinProjects Parent'

    def get_child(self):
        return KotlinProjects.objects.all()


class RProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'RProjects Parent'

    def get_child(self):
        return RProjects.objects.all()


class CSharpProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CSharpProjects Parent'

    def get_child(self):
        return CSharpProjects.objects.all()


class SwiftProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SwiftProjects Parent'

    def get_child(self):
        return SwiftProjects.objects.all()


class JavaScriptProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaScriptProjects Parent'

    def get_child(self):
        return JavaScriptProjects.objects.all()


class AndroidProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'AndroidProjects Parent'

    def get_child(self):
        return AndroidProjects.objects.all()


class PHPProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PHPProjects Parent'

    def get_child(self):
        return PHPProjects.objects.all()


class DotNetProjectsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DotNetProjects Parent'

    def get_child(self):
        return DotNetProjects.objects.all()


# Child
class CProjects(TutCommon):
    parent = models.ForeignKey(CProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:cprojectsdetail", kwargs={"slug": self.slug})}'


class CPlusProjects(TutCommon):
    parent = models.ForeignKey(CPlusProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CPlusProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:cplusprojectsdetail", kwargs={"slug": self.slug})}'


class PythonProjects(TutCommon):
    parent = models.ForeignKey(PythonProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PythonProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:pythonprojectsdetail", kwargs={"slug": self.slug})}'


class JavaProjects(TutCommon):
    parent = models.ForeignKey(JavaProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:javaprojectsdetail", kwargs={"slug": self.slug})}'


class KotlinProjects(TutCommon):
    parent = models.ForeignKey(KotlinProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'KotlinProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:kotlinprojectsdetail", kwargs={"slug": self.slug})}'


class RProjects(TutCommon):
    parent = models.ForeignKey(RProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'RProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:rprojectsdetail", kwargs={"slug": self.slug})}'


class CSharpProjects(TutCommon):
    parent = models.ForeignKey(CSharpProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CSharpProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:csharpprojectsdetail", kwargs={"slug": self.slug})}'


class SwiftProjects(TutCommon):
    parent = models.ForeignKey(SwiftProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SwiftProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:swiftprojectsdetail", kwargs={"slug": self.slug})}'


class JavaScriptProjects(TutCommon):
    parent = models.ForeignKey(JavaScriptProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaScriptProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:javascriptprojectsdetail", kwargs={"slug": self.slug})}'


class AndroidProjects(TutCommon):
    parent = models.ForeignKey(AndroidProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'AndroidProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:androidprojectsdetail", kwargs={"slug": self.slug})}'


class PHPProjects(TutCommon):
    parent = models.ForeignKey(PHPProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PHPProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:phpprojectsdetail", kwargs={"slug": self.slug})}'


class DotNetProjects(TutCommon):
    parent = models.ForeignKey(DotNetProjectsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DotNetProjects'

    def get_absolute_url(self):
        return f'{reverse_lazy("Projects:dotnetprojectsdetail", kwargs={"slug": self.slug})}'


# Like Counter
class CProjectsLike(LikeCommon):
    post = models.ForeignKey(CProjects, on_delete=models.CASCADE)


class CPlusProjectsLike(LikeCommon):
    post = models.ForeignKey(CPlusProjects, on_delete=models.CASCADE)


class PythonProjectsLike(LikeCommon):
    post = models.ForeignKey(PythonProjects, on_delete=models.CASCADE)


class JavaProjectsLike(LikeCommon):
    post = models.ForeignKey(JavaProjects, on_delete=models.CASCADE)


class KotlinProjectsLike(LikeCommon):
    post = models.ForeignKey(KotlinProjects, on_delete=models.CASCADE)


class RProjectsLike(LikeCommon):
    post = models.ForeignKey(RProjects, on_delete=models.CASCADE)


class CSharpProjectsLike(LikeCommon):
    post = models.ForeignKey(CSharpProjects, on_delete=models.CASCADE)


class SwiftProjectsLike(LikeCommon):
    post = models.ForeignKey(SwiftProjects, on_delete=models.CASCADE)


class JavaScriptProjectsLike(LikeCommon):
    post = models.ForeignKey(JavaScriptProjects, on_delete=models.CASCADE)


class AndroidProjectsLike(LikeCommon):
    post = models.ForeignKey(AndroidProjects, on_delete=models.CASCADE)


class PHPProjectsLike(LikeCommon):
    post = models.ForeignKey(PHPProjects, on_delete=models.CASCADE)


class DotNetProjectsLike(LikeCommon):
    post = models.ForeignKey(DotNetProjects, on_delete=models.CASCADE)
