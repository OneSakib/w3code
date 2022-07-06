from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.
# Parent
class HTMLsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'HTMLs Parent'

    def get_child(self):
        return HTMLs.objects.all()


class CSSsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CSSs Parent'

    def get_child(self):
        return CSSs.objects.all()


class LaravelsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Laravels Parent'

    def get_child(self):
        return Laravels.objects.all()


class WordpressParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Wordpress Parent'

    def get_child(self):
        return Wordpress.objects.all()


class JSONsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JSONs Parent'

    def get_child(self):
        return JSONs.objects.all()


class AjaxsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Ajaxs Parent'

    def get_child(self):
        return Ajaxs.objects.all()


class BootstrapsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Bootstraps Parent'

    def get_child(self):
        return Bootstraps.objects.all()


# web Technology
class HTMLs(TutCommon):
    parent = models.ForeignKey(HTMLsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'HTMLs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:htmldetail", kwargs={"slug": self.slug})}'


class CSSs(TutCommon):
    parent = models.ForeignKey(CSSsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CSSs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:cssdetail", kwargs={"slug": self.slug})}'


class Laravels(TutCommon):
    parent = models.ForeignKey(LaravelsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Laravels'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:laraveldetail", kwargs={"slug": self.slug})}'


class Wordpress(TutCommon):
    parent = models.ForeignKey(WordpressParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Wordpress'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:wordpressdetail", kwargs={"slug": self.slug})}'


class JSONs(TutCommon):
    parent = models.ForeignKey(JSONsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JSONs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:jsondetail", kwargs={"slug": self.slug})}'


class Ajaxs(TutCommon):
    parent = models.ForeignKey(AjaxsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Ajaxs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:ajaxdetail", kwargs={"slug": self.slug})}'


class Bootstraps(TutCommon):
    parent = models.ForeignKey(BootstrapsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Bootstraps'

    def get_absolute_url(self):
        return f'{reverse_lazy("Web:bootstrapdetail", kwargs={"slug": self.slug})}'


# Like Counter
class HTMLsLike(LikeCommon):
    post = models.ForeignKey(HTMLs, on_delete=models.CASCADE)


class CSSsLike(LikeCommon):
    post = models.ForeignKey(CSSs, on_delete=models.CASCADE)


class LaravelsLike(LikeCommon):
    post = models.ForeignKey(Laravels, on_delete=models.CASCADE)


class WordpressLike(LikeCommon):
    post = models.ForeignKey(Wordpress, on_delete=models.CASCADE)


class JSONsLike(LikeCommon):
    post = models.ForeignKey(JSONs, on_delete=models.CASCADE)


class AjaxsLike(LikeCommon):
    post = models.ForeignKey(Ajaxs, on_delete=models.CASCADE)


class BootstrapsLike(LikeCommon):
    post = models.ForeignKey(Bootstraps, on_delete=models.CASCADE)
