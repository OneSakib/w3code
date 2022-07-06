from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.

# Parent
class DockerParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Docker Parent'

    def get_child(self):
        return Docker.objects.all()


class GitsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Gits Parent'

    def get_child(self):
        return Gits.objects.all()


class GithubsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Githubs Parent'

    def get_child(self):
        return Githubs.objects.all()


# Versioning Control
class Docker(TutCommon):
    parent = models.ForeignKey(DockerParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Docker'

    def get_absolute_url(self):
        return f'{reverse_lazy("VC:dockerdetail", kwargs={"slug": self.slug})}'


class Gits(TutCommon):
    parent = models.ForeignKey(GitsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Gits'

    def get_absolute_url(self):
        return f'{reverse_lazy("VC:gitdetail", kwargs={"slug": self.slug})}'


class Githubs(TutCommon):
    parent = models.ForeignKey(GithubsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Githubs'

    def get_absolute_url(self):
        return f'{reverse_lazy("VC:githubdetail", kwargs={"slug": self.slug})}'


# Like Counter
class DockerLike(LikeCommon):
    post = models.ForeignKey(Docker, on_delete=models.CASCADE)


class GitsLike(LikeCommon):
    post = models.ForeignKey(Gits, on_delete=models.CASCADE)


class GithubsLike(LikeCommon):
    post = models.ForeignKey(Githubs, on_delete=models.CASCADE)
