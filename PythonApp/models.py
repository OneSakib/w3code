from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Python Tut
class Django(TutCommon):
    class Meta:
        verbose_name_plural = 'Django'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:djangodetail", kwargs={"slug": self.slug})}'


class Flask(TutCommon):
    class Meta:
        verbose_name_plural = 'Flask'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:flaskdetail", kwargs={"slug": self.slug})}'


class MachineLearning(TutCommon):
    class Meta:
        verbose_name_plural = 'MachineLearning'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:machinelearningdetail", kwargs={"slug": self.slug})}'


class Numpys(TutCommon):
    class Meta:
        verbose_name_plural = 'Numpys'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:numpydetail", kwargs={"slug": self.slug})}'


class Tkinters(TutCommon):
    class Meta:
        verbose_name_plural = 'Tkinters'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:tkinterdetail", kwargs={"slug": self.slug})}'


class Pytorchs(TutCommon):
    class Meta:
        verbose_name_plural = 'Pytorchs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:pytorchdetail", kwargs={"slug": self.slug})}'


class Pygames(TutCommon):
    class Meta:
        verbose_name_plural = 'Pygames'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:pygamedetail", kwargs={"slug": self.slug})}'


class Scipys(TutCommon):
    class Meta:
        verbose_name_plural = 'Scipys'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:scipydetail", kwargs={"slug": self.slug})}'


class Pandass(TutCommon):
    class Meta:
        verbose_name_plural = 'Pandass'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:pandasdetail", kwargs={"slug": self.slug})}'


class OpenCVs(TutCommon):
    class Meta:
        verbose_name_plural = 'OpenCVs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:opencvdetail", kwargs={"slug": self.slug})}'


class Matplotlibs(TutCommon):
    class Meta:
        verbose_name_plural = 'Matplotlibs'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:matplotlibdetail", kwargs={"slug": self.slug})}'


class Seleniums(TutCommon):
    class Meta:
        verbose_name_plural = 'Seleniums'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:seleniumdetail", kwargs={"slug": self.slug})}'


class Kivys(TutCommon):
    class Meta:
        verbose_name_plural = 'Kivys'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:kivydetail", kwargs={"slug": self.slug})}'


class Jupyters(TutCommon):
    class Meta:
        verbose_name_plural = 'Jupyters'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:jupyterdetail", kwargs={"slug": self.slug})}'


class DataScience(TutCommon):
    class Meta:
        verbose_name_plural = 'DataScience'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:datasciencedetail", kwargs={"slug": self.slug})}'


class DeepLearning(TutCommon):
    class Meta:
        verbose_name_plural = 'DeepLearning'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:deeplearningdetail", kwargs={"slug": self.slug})}'


class Pillows(TutCommon):
    class Meta:
        verbose_name_plural = 'Pillows'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:pillowdetail", kwargs={"slug": self.slug})}'


class Tensorflows(TutCommon):
    class Meta:
        verbose_name_plural = 'Tensorflows'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Python:tensorflowdetail", kwargs={"slug": self.slug})}'


# Comments
class DjangoComments(Comments):
    post = models.ForeignKey(Django, on_delete=models.CASCADE, related_name='DjangoComments')

    class Meta:
        verbose_name_plural = 'DjangoComments'


class FlaskComments(Comments):
    post = models.ForeignKey(Flask, on_delete=models.CASCADE, related_name='FlaskComments')

    class Meta:
        verbose_name_plural = 'FlaskComments'


class MachineLearningComments(Comments):
    post = models.ForeignKey(MachineLearning, on_delete=models.CASCADE, related_name='MachineLearningComments')

    class Meta:
        verbose_name_plural = 'MachineLearningComments'


class NumpysComments(Comments):
    post = models.ForeignKey(Numpys, on_delete=models.CASCADE, related_name='NumpysComments')

    class Meta:
        verbose_name_plural = 'NumpysComments'


class TkintersComments(Comments):
    post = models.ForeignKey(Tkinters, on_delete=models.CASCADE, related_name='TkintersComments')

    class Meta:
        verbose_name_plural = 'TkintersComments'


class PytorchsComments(Comments):
    post = models.ForeignKey(Pytorchs, on_delete=models.CASCADE, related_name='PytorchsComments')

    class Meta:
        verbose_name_plural = 'PytorchsComments'


class PygamesComments(Comments):
    post = models.ForeignKey(Pygames, on_delete=models.CASCADE, related_name='PygamesComments')

    class Meta:
        verbose_name_plural = 'PygamesComments'


class ScipysComments(Comments):
    post = models.ForeignKey(Scipys, on_delete=models.CASCADE, related_name='ScipysComments')

    class Meta:
        verbose_name_plural = 'ScipysComments'


class PandassComments(Comments):
    post = models.ForeignKey(Pandass, on_delete=models.CASCADE, related_name='PandassComments')

    class Meta:
        verbose_name_plural = 'PandassComments'


class OpenCVsComments(Comments):
    post = models.ForeignKey(OpenCVs, on_delete=models.CASCADE, related_name='OpenCVsComments')

    class Meta:
        verbose_name_plural = 'OpenCVsComments'


class MatplotlibsComments(Comments):
    post = models.ForeignKey(Matplotlibs, on_delete=models.CASCADE, related_name='MatplotlibsComments')

    class Meta:
        verbose_name_plural = 'MatplotlibsComments'


class SeleniumsComments(Comments):
    post = models.ForeignKey(Seleniums, on_delete=models.CASCADE, related_name='SeleniumsComments')

    class Meta:
        verbose_name_plural = 'SeleniumsComments'


class KivysComments(Comments):
    post = models.ForeignKey(Kivys, on_delete=models.CASCADE, related_name='KivysComments')

    class Meta:
        verbose_name_plural = 'KivysComments'


class JupytersComments(Comments):
    post = models.ForeignKey(Jupyters, on_delete=models.CASCADE, related_name='JupytersComments')

    class Meta:
        verbose_name_plural = 'JupytersComments'


class DataScienceComments(Comments):
    post = models.ForeignKey(DataScience, on_delete=models.CASCADE, related_name='DataScienceComments')

    class Meta:
        verbose_name_plural = 'DataScienceComments'


class DeepLearningComments(Comments):
    post = models.ForeignKey(DeepLearning, on_delete=models.CASCADE, related_name='DeepLearningComments')

    class Meta:
        verbose_name_plural = 'DeepLearningComments'


class PillowsComments(Comments):
    post = models.ForeignKey(Pillows, on_delete=models.CASCADE, related_name='PillowsComments')

    class Meta:
        verbose_name_plural = 'PillowsComments'


class TensorflowsComments(Comments):
    post = models.ForeignKey(Tensorflows, on_delete=models.CASCADE, related_name='TensorflowsComments')

    class Meta:
        verbose_name_plural = 'TensorflowsComments'
