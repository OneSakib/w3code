from django.db import models
from MainApp.models import TutCommon, Comments
from django.urls import reverse_lazy


# Create your models here.


# Hosting Tut
class DigitalOcean(TutCommon):
    class Meta:
        verbose_name_plural = 'DigitalOcean'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:digitaloceandetail", kwargs={"slug": self.slug})}'


class MSAzure(TutCommon):
    class Meta:
        verbose_name_plural = 'MSAzure'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:msazuredetail", kwargs={"slug": self.slug})}'


class AWS(TutCommon):
    class Meta:
        verbose_name_plural = 'AWS'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:awsdetail", kwargs={"slug": self.slug})}'


class PythonAnywhere(TutCommon):
    class Meta:
        verbose_name_plural = 'PythonAnywhere'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:pythonanywheredetail", kwargs={"slug": self.slug})}'


class HerokuApp(TutCommon):
    class Meta:
        verbose_name_plural = 'HerokuApp'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:herokuappdetail", kwargs={"slug": self.slug})}'


class GithubHost(TutCommon):
    class Meta:
        verbose_name_plural = 'GithubHost'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:githubhostdetail", kwargs={"slug": self.slug})}'


class BlueHost(TutCommon):
    class Meta:
        verbose_name_plural = 'BlueHost'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:bluehostdetail", kwargs={"slug": self.slug})}'


class HostGator(TutCommon):
    class Meta:
        verbose_name_plural = 'HostGator'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:hostgatordetail", kwargs={"slug": self.slug})}'


class InMotionHosting(TutCommon):
    class Meta:
        verbose_name_plural = 'InMotionHosting'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:inmotionhostingdetail", kwargs={"slug": self.slug})}'


class A2Hosting(TutCommon):
    class Meta:
        verbose_name_plural = 'A2Hosting'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:a2hostingdetail", kwargs={"slug": self.slug})}'


class GreenGeeks(TutCommon):
    class Meta:
        verbose_name_plural = 'GreenGeeks'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:greengeeksdetail", kwargs={"slug": self.slug})}'


class Hostinger(TutCommon):
    class Meta:
        verbose_name_plural = 'Hostinger'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Hosting:hostingerdetail", kwargs={"slug": self.slug})}'


class GoDaddy(TutCommon):
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
