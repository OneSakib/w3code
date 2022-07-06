from django.db import models
from MainApp.models import TutCommon, LikeCommon, TutCommonParent
from django.urls import reverse_lazy


# Create your models here.
class ServletsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Servlets Parent'

    def get_child(self):
        return Servlets.objects.all()


class JSPsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JSPs Parent'

    def get_child(self):
        return JSPs.objects.all()


class SpringBootParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SpringBoot Parent'

    def get_child(self):
        return SpringBoot.objects.all()


class SpringFrameworkParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SpringFramework Parent'

    def get_child(self):
        return SpringFramework.objects.all()


class HibernatesParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Hibernates Parent'

    def get_child(self):
        return Hibernates.objects.all()


class JavaSwingsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaSwings Parent'

    def get_child(self):
        return JavaSwings.objects.all()


class JavaFXsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaFXs Parent'

    def get_child(self):
        return JavaFXs.objects.all()


class JavaAWTParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaAWT Parent'

    def get_child(self):
        return JavaAWT.objects.all()


class CollectionsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Collections Parent'

    def get_child(self):
        return Collections.objects.all()


class JavaDateParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaDate Parent'

    def get_child(self):
        return JavaDate.objects.all()


class JavaIOParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaIO Parent'

    def get_child(self):
        return JavaIO.objects.all()


# Child
# Java
class Servlets(TutCommon):
    parent = models.ForeignKey(ServletsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Servlets'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:servletdetail", kwargs={"slug": self.slug})}'


class JSPs(TutCommon):
    parent = models.ForeignKey(JSPsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JSPs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:jspdetail", kwargs={"slug": self.slug})}'


class SpringBoot(TutCommon):
    parent = models.ForeignKey(SpringBootParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SpringBoot'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:springbootdetail", kwargs={"slug": self.slug})}'


class SpringFramework(TutCommon):
    parent = models.ForeignKey(SpringFrameworkParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SpringFramework'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:springframeworkdetail", kwargs={"slug": self.slug})}'


class Hibernates(TutCommon):
    parent = models.ForeignKey(HibernatesParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Hibernates'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:hibernatedetail", kwargs={"slug": self.slug})}'


class JavaSwings(TutCommon):
    parent = models.ForeignKey(JavaSwingsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaSwings'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javaswingdetail", kwargs={"slug": self.slug})}'


class JavaFXs(TutCommon):
    parent = models.ForeignKey(JavaFXsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaFXs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javafxdetail", kwargs={"slug": self.slug})}'


class JavaAWT(TutCommon):
    parent = models.ForeignKey(JavaAWTParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaAWT'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javaawtdetail", kwargs={"slug": self.slug})}'


class Collections(TutCommon):
    parent = models.ForeignKey(CollectionsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Collections'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javacollectionsdetail", kwargs={"slug": self.slug})}'


class JavaDate(TutCommon):
    parent = models.ForeignKey(JavaDateParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaDate'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javadatedetail", kwargs={"slug": self.slug})}'


class JavaIO(TutCommon):
    parent = models.ForeignKey(JavaIOParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaIO'

    def get_absolute_url(self):
        return f'{reverse_lazy("Java:javaiodetail", kwargs={"slug": self.slug})}'


# Like Counter
class ServletsLike(LikeCommon):
    post = models.ForeignKey(Servlets, on_delete=models.CASCADE)


class JSPsLike(LikeCommon):
    post = models.ForeignKey(JSPs, on_delete=models.CASCADE)


class SpringBootLike(LikeCommon):
    post = models.ForeignKey(SpringBoot, on_delete=models.CASCADE)


class SpringFrameworkLike(LikeCommon):
    post = models.ForeignKey(SpringFramework, on_delete=models.CASCADE)


class HibernatesLike(LikeCommon):
    post = models.ForeignKey(Hibernates, on_delete=models.CASCADE)


class JavaSwingsLike(LikeCommon):
    post = models.ForeignKey(JavaSwings, on_delete=models.CASCADE)


class JavaFXsLike(LikeCommon):
    post = models.ForeignKey(JavaFXs, on_delete=models.CASCADE)


class JavaAWTLike(LikeCommon):
    post = models.ForeignKey(JavaAWT, on_delete=models.CASCADE)


class CollectionsLike(LikeCommon):
    post = models.ForeignKey(Collections, on_delete=models.CASCADE)


class JavaDateLike(LikeCommon):
    post = models.ForeignKey(JavaDate, on_delete=models.CASCADE)


class JavaIOLike(LikeCommon):
    post = models.ForeignKey(JavaIO, on_delete=models.CASCADE)
