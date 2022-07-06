from django.db import models
from MainApp.models import TutCommon, LikeCommon, TutCommonParent
from django.urls import reverse_lazy


# Create your models here.

# Parent
class JqueryParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Jquery Parent'

    def get_child(self):
        return Jquery.objects.all()


class AngularjsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Angularjs Parent'

    def get_child(self):
        return Angularjs.objects.all()


class NodejsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Nodejs Parent'

    def get_child(self):
        return Nodejs.objects.all()


class ExpressjsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Expressjs Parent'

    def get_child(self):
        return Expressjs.objects.all()


class ReactjsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Reactjs Parent'

    def get_child(self):
        return Reactjs.objects.all()


class TypeScriptsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'TypeScripts Parent'

    def get_child(self):
        return TypeScripts.objects.all()


class VUEjsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'VUEjs Parent'

    def get_child(self):
        return VUEjs.objects.all()


# Child
# JavaScript
class Jquery(TutCommon):
    parent = models.ForeignKey(JqueryParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Jquery'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:jquerydetail", kwargs={"slug": self.slug})}'


class Angularjs(TutCommon):
    parent = models.ForeignKey(AngularjsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Angularjs'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:angulardetail", kwargs={"slug": self.slug})}'


class Nodejs(TutCommon):
    parent = models.ForeignKey(NodejsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Nodejs'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:nodejsdetail", kwargs={"slug": self.slug})}'


class Expressjs(TutCommon):
    parent = models.ForeignKey(ExpressjsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Expressjs'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:expressjsdetail", kwargs={"slug": self.slug})}'


class Reactjs(TutCommon):
    parent = models.ForeignKey(ReactjsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Reactjs'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:reactjsdetail", kwargs={"slug": self.slug})}'


class TypeScripts(TutCommon):
    parent = models.ForeignKey(TypeScriptsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'TypeScripts'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:typescriptdetail", kwargs={"slug": self.slug})}'


class VUEjs(TutCommon):
    parent = models.ForeignKey(VUEjsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'VUEjs'

    def get_absolute_url(self):
        return f'{reverse_lazy("JavaScript:vuejsdetail", kwargs={"slug": self.slug})}'


# Like Counter
class JqueryLike(LikeCommon):
    post = models.ForeignKey(Jquery, on_delete=models.CASCADE)


class AngularjsLike(LikeCommon):
    post = models.ForeignKey(Angularjs, on_delete=models.CASCADE)


class NodejsLike(LikeCommon):
    post = models.ForeignKey(Nodejs, on_delete=models.CASCADE)


class ExpressjsLike(LikeCommon):
    post = models.ForeignKey(Expressjs, on_delete=models.CASCADE)


class ReactjsLike(LikeCommon):
    post = models.ForeignKey(Reactjs, on_delete=models.CASCADE)


class TypeScriptsLike(LikeCommon):
    post = models.ForeignKey(TypeScripts, on_delete=models.CASCADE)


class VUEjsLike(LikeCommon):
    post = models.ForeignKey(VUEjs, on_delete=models.CASCADE)
