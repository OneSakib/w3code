from django.db import models
from MainApp.models import TutCommon, Comments, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.


# Parent
class DigitalOceanParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DigitalOcean Parent'

    def get_child(self):
        return DigitalOcean.objects.all()


class MSAzureParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MSAzure Parent'

    def get_child(self):
        return MSAzure.objects.all()


class AWSParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'AWS Parent'

    def get_child(self):
        return AWS.objects.all()


class PythonAnywhereParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PythonAnywhere Parent'

    def get_child(self):
        return PythonAnywhere.objects.all()


class HerokuAppParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'HerokuApp Parent'

    def get_child(self):
        return HerokuApp.objects.all()


class GithubHostParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'GithubHost Parent'

    def get_child(self):
        return GithubHost.objects.all()


class BlueHostParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'BlueHost Parent'

    def get_child(self):
        return BlueHost.objects.all()


class HostGatorParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'HostGator Parent'

    def get_child(self):
        return HostGator.objects.all()


class InMotionHostingParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'InMotionHosting Parent'

    def get_child(self):
        return InMotionHosting.objects.all()


class A2HostingParent(TutCommonParent):
    class Meta:
        verbose_name_plural = ' A2Hosting Parent'

    def get_child(self):
        return A2Hosting.objects.all()


class GreenGeeksParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'GreenGeeks Parent'

    def get_child(self):
        return GreenGeeks.objects.all()


class HostingerParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Hostinger Parent'

    def get_child(self):
        return Hostinger.objects.all()


class GoDaddyParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'GoDaddy Parent'

    def get_child(self):
        return GoDaddy.objects.all()


# Child
# Hosting Tut
class DigitalOcean(TutCommon):
    parent = models.ForeignKey(DigitalOceanParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DigitalOcean'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:digitaloceandetail", kwargs={"slug": self.slug})}'


class MSAzure(TutCommon):
    parent = models.ForeignKey(MSAzureParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MSAzure'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:msazuredetail", kwargs={"slug": self.slug})}'


class AWS(TutCommon):
    parent = models.ForeignKey(AWSParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'AWS'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:awsdetail", kwargs={"slug": self.slug})}'


class PythonAnywhere(TutCommon):
    parent = models.ForeignKey(PythonAnywhereParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PythonAnywhere'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:pythonanywheredetail", kwargs={"slug": self.slug})}'


class HerokuApp(TutCommon):
    parent = models.ForeignKey(HerokuAppParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'HerokuApp'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:herokuappdetail", kwargs={"slug": self.slug})}'


class GithubHost(TutCommon):
    parent = models.ForeignKey(GithubHostParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'GithubHost'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:githubhostdetail", kwargs={"slug": self.slug})}'


class BlueHost(TutCommon):
    parent = models.ForeignKey(BlueHostParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'BlueHost'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:bluehostdetail", kwargs={"slug": self.slug})}'


class HostGator(TutCommon):
    parent = models.ForeignKey(HostGatorParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'HostGator'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:hostgatordetail", kwargs={"slug": self.slug})}'


class InMotionHosting(TutCommon):
    parent = models.ForeignKey(InMotionHostingParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'InMotionHosting'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:inmotionhostingdetail", kwargs={"slug": self.slug})}'


class A2Hosting(TutCommon):
    parent = models.ForeignKey(A2HostingParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'A2Hosting'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:a2hostingdetail", kwargs={"slug": self.slug})}'


class GreenGeeks(TutCommon):
    parent = models.ForeignKey(GreenGeeksParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'GreenGeeks'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:greengeeksdetail", kwargs={"slug": self.slug})}'


class Hostinger(TutCommon):
    parent = models.ForeignKey(HostingerParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Hostinger'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:hostingerdetail", kwargs={"slug": self.slug})}'


class GoDaddy(TutCommon):
    parent = models.ForeignKey(GoDaddyParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'GoDaddy'

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:godaddydetail", kwargs={"slug": self.slug})}'


# Comments

class DigitalOceanComments(Comments):
    post = models.ForeignKey(DigitalOcean, on_delete=models.CASCADE, related_name='DigitalOceancomments')

    class Meta:
        verbose_name_plural = 'DigitalOceanComments'


class MSAzureComments(Comments):
    post = models.ForeignKey(MSAzure, on_delete=models.CASCADE, related_name='MSAzureCom')

    class Meta:
        verbose_name_plural = 'MSAzureComments'


class AWSComments(Comments):
    post = models.ForeignKey(AWS, on_delete=models.CASCADE, related_name='AWSComments')

    class Meta:
        verbose_name_plural = 'AWSComments'


class PythonAnywhereComments(Comments):
    post = models.ForeignKey(PythonAnywhere, on_delete=models.CASCADE, related_name='PythonAnywhereComments')

    class Meta:
        verbose_name_plural = 'PythonAnywhereComments'


class HerokuAppComments(Comments):
    post = models.ForeignKey(HerokuApp, on_delete=models.CASCADE, related_name='HerokuAppComments')

    class Meta:
        verbose_name_plural = 'HerokuAppComments'


class GithubHostComments(Comments):
    post = models.ForeignKey(GithubHost, on_delete=models.CASCADE, related_name='GithubHostComments')

    class Meta:
        verbose_name_plural = 'GithubHostComments'


class BlueHostComments(Comments):
    post = models.ForeignKey(BlueHost, on_delete=models.CASCADE, related_name='BlueHostComments')

    class Meta:
        verbose_name_plural = 'BlueHostComments'


class HostGatorComments(Comments):
    post = models.ForeignKey(HostGator, on_delete=models.CASCADE, related_name='HostGatorComments')

    class Meta:
        verbose_name_plural = 'HostGatorComments'


class InMotionHostingComments(Comments):
    post = models.ForeignKey(InMotionHosting, on_delete=models.CASCADE, related_name='InMotionHostingComments')

    class Meta:
        verbose_name_plural = 'InMotionHostingComments'


class A2HostingComments(Comments):
    post = models.ForeignKey(A2Hosting, on_delete=models.CASCADE, related_name='A2HostingComments')

    class Meta:
        verbose_name_plural = 'A2HostingComments'


class GreenGeeksComments(Comments):
    post = models.ForeignKey(GreenGeeks, on_delete=models.CASCADE, related_name='GreenGeeksComments')

    class Meta:
        verbose_name_plural = 'GreenGeeksComments'


class HostingerComments(Comments):
    post = models.ForeignKey(Hostinger, on_delete=models.CASCADE, related_name='HostingerComments')

    class Meta:
        verbose_name_plural = 'HostingerComments'


class GoDaddyComments(Comments):
    post = models.ForeignKey(GoDaddy, on_delete=models.CASCADE, related_name='GoDaddyComments')

    class Meta:
        verbose_name_plural = 'GoDaddyComments'


# Like button
class DigitalOceanLike(LikeCommon):
    post = models.ForeignKey(DigitalOcean, on_delete=models.CASCADE)


class MSAzureLike(LikeCommon):
    post = models.ForeignKey(MSAzure, on_delete=models.CASCADE)


class AWSLike(LikeCommon):
    post = models.ForeignKey(AWS, on_delete=models.CASCADE)


class PythonAnywhereLike(LikeCommon):
    post = models.ForeignKey(PythonAnywhere, on_delete=models.CASCADE)


class HerokuAppLike(LikeCommon):
    post = models.ForeignKey(HerokuApp, on_delete=models.CASCADE)


class GithubHostLike(LikeCommon):
    post = models.ForeignKey(GithubHost, on_delete=models.CASCADE)


class BlueHostLike(LikeCommon):
    post = models.ForeignKey(BlueHost, on_delete=models.CASCADE)


class HostGatorLike(LikeCommon):
    post = models.ForeignKey(HostGator, on_delete=models.CASCADE)


class InMotionHostingLike(LikeCommon):
    post = models.ForeignKey(InMotionHosting, on_delete=models.CASCADE)


class A2HostingLike(LikeCommon):
    post = models.ForeignKey(A2Hosting, on_delete=models.CASCADE)


class GreenGeeksLike(LikeCommon):
    post = models.ForeignKey(GreenGeeks, on_delete=models.CASCADE)


class HostingerLike(LikeCommon):
    post = models.ForeignKey(Hostinger, on_delete=models.CASCADE)


class GoDaddyLike(LikeCommon):
    post = models.ForeignKey(GoDaddy, on_delete=models.CASCADE)
