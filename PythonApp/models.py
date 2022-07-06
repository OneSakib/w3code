from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.

# Parent
class DjangoParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Django Parent'

    def get_child(self):
        return Django.objects.all()


class RestApiParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'RestApi Parent'

    def get_child(self):
        return RestApi.objects.all()


class FlaskParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Flask Parent'

    def get_child(self):
        return Flask.objects.all()


class MachineLearningParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MachineLearning Parent'

    def get_child(self):
        return MachineLearning.objects.all()


class NumpysParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Numpys Parent'

    def get_child(self):
        return Numpys.objects.all()


class TkintersParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Tkinters Parent'

    def get_child(self):
        return Tkinters.objects.all()


class PytorchsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Pytorchs Parent'

    def get_child(self):
        return Pytorchs.objects.all()


class PygamesParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Pygames Parent'

    def get_child(self):
        return Pygames.objects.all()


class ScipysParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Scipys Parent'

    def get_child(self):
        return Scipys.objects.all()


class PandassParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Pandass Parent'

    def get_child(self):
        return Pandass.objects.all()


class OpenCVsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'OpenCVs Parent'

    def get_child(self):
        return OpenCVs.objects.all()


class MatplotlibsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Matplotlibs Parent'

    def get_child(self):
        return Matplotlibs.objects.all()


class SeleniumsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Seleniums Parent'

    def get_child(self):
        return Seleniums.objects.all()


class KivysParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Kivys Parent'

    def get_child(self):
        return Kivys.objects.all()


class JupytersParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Jupyters Parent'

    def get_child(self):
        return Jupyters.objects.all()


class DataScienceParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DataScience Parent'

    def get_child(self):
        return DataScience.objects.all()


class DeepLearningParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DeepLearning Parent'

    def get_child(self):
        return DeepLearning.objects.all()


class PillowsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Pillows Parent'

    def get_child(self):
        return Pillows.objects.all()


class TensorflowsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Tensorflows Parent'

    def get_child(self):
        return Tensorflows.objects.all()


class DSPythonParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DSPython Parent'

    def get_child(self):
        return DSPython.objects.all()


# Python Tut
class Django(TutCommon):
    parent = models.ForeignKey(DjangoParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Django'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:djangodetail", kwargs={"slug": self.slug})}'


class RestApi(TutCommon):
    parent = models.ForeignKey(RestApiParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'RestApi'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:restapidetail", kwargs={"slug": self.slug})}'


class Flask(TutCommon):
    parent = models.ForeignKey(FlaskParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Flask'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:flaskdetail", kwargs={"slug": self.slug})}'


class MachineLearning(TutCommon):
    parent = models.ForeignKey(MachineLearningParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MachineLearning'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:machinelearningdetail", kwargs={"slug": self.slug})}'


class Numpys(TutCommon):
    parent = models.ForeignKey(NumpysParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Numpys'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:numpydetail", kwargs={"slug": self.slug})}'


class Tkinters(TutCommon):
    parent = models.ForeignKey(TkintersParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Tkinters'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:tkinterdetail", kwargs={"slug": self.slug})}'


class Pytorchs(TutCommon):
    parent = models.ForeignKey(PytorchsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Pytorchs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pytorchdetail", kwargs={"slug": self.slug})}'


class Pygames(TutCommon):
    parent = models.ForeignKey(PygamesParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Pygames'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pygamedetail", kwargs={"slug": self.slug})}'


class Scipys(TutCommon):
    parent = models.ForeignKey(ScipysParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Scipys'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:scipydetail", kwargs={"slug": self.slug})}'


class Pandass(TutCommon):
    parent = models.ForeignKey(PandassParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Pandass'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pandasdetail", kwargs={"slug": self.slug})}'


class OpenCVs(TutCommon):
    parent = models.ForeignKey(OpenCVsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'OpenCVs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:opencvdetail", kwargs={"slug": self.slug})}'


class Matplotlibs(TutCommon):
    parent = models.ForeignKey(MatplotlibsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Matplotlibs'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:matplotlibdetail", kwargs={"slug": self.slug})}'


class Seleniums(TutCommon):
    parent = models.ForeignKey(SeleniumsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Seleniums'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:seleniumdetail", kwargs={"slug": self.slug})}'


class Kivys(TutCommon):
    parent = models.ForeignKey(KivysParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Kivys'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:kivydetail", kwargs={"slug": self.slug})}'


class Jupyters(TutCommon):
    parent = models.ForeignKey(JupytersParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Jupyters'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:jupyterdetail", kwargs={"slug": self.slug})}'


class DataScience(TutCommon):
    parent = models.ForeignKey(DataScienceParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DataScience'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:datasciencedetail", kwargs={"slug": self.slug})}'


class DeepLearning(TutCommon):
    parent = models.ForeignKey(DeepLearningParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DeepLearning'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:deeplearningdetail", kwargs={"slug": self.slug})}'


class Pillows(TutCommon):
    parent = models.ForeignKey(PillowsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Pillows'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:pillowdetail", kwargs={"slug": self.slug})}'


class Tensorflows(TutCommon):
    parent = models.ForeignKey(TensorflowsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Tensorflows'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:tensorflowdetail", kwargs={"slug": self.slug})}'


class DSPython(TutCommon):
    parent = models.ForeignKey(DSPythonParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DSPython'

    def get_absolute_url(self):
        return f'{reverse_lazy("Python:dspythondetail", kwargs={"slug": self.slug})}'


# Like Counter
class DjangoLike(LikeCommon):
    post = models.ForeignKey(Django, on_delete=models.CASCADE)


class RestApiLike(LikeCommon):
    post = models.ForeignKey(RestApi, on_delete=models.CASCADE)


class FlaskLike(LikeCommon):
    post = models.ForeignKey(Flask, on_delete=models.CASCADE)


class MachineLearningLike(LikeCommon):
    post = models.ForeignKey(MachineLearning, on_delete=models.CASCADE)


class NumpysLike(LikeCommon):
    post = models.ForeignKey(Numpys, on_delete=models.CASCADE)


class TkintersLike(LikeCommon):
    post = models.ForeignKey(Tkinters, on_delete=models.CASCADE)


class PytorchsLike(LikeCommon):
    post = models.ForeignKey(Pytorchs, on_delete=models.CASCADE)


class PygamesLike(LikeCommon):
    post = models.ForeignKey(Pygames, on_delete=models.CASCADE)


class ScipysLike(LikeCommon):
    post = models.ForeignKey(Scipys, on_delete=models.CASCADE)


class PandassLike(LikeCommon):
    post = models.ForeignKey(Pandass, on_delete=models.CASCADE)


class OpenCVsLike(LikeCommon):
    post = models.ForeignKey(OpenCVs, on_delete=models.CASCADE)


class MatplotlibsLike(LikeCommon):
    post = models.ForeignKey(Matplotlibs, on_delete=models.CASCADE)


class SeleniumsLike(LikeCommon):
    post = models.ForeignKey(Seleniums, on_delete=models.CASCADE)


class KivysLike(LikeCommon):
    post = models.ForeignKey(Kivys, on_delete=models.CASCADE)


class JupytersLike(LikeCommon):
    post = models.ForeignKey(Jupyters, on_delete=models.CASCADE)


class DataScienceLike(LikeCommon):
    post = models.ForeignKey(DataScience, on_delete=models.CASCADE)


class DeepLearningLike(LikeCommon):
    post = models.ForeignKey(DeepLearning, on_delete=models.CASCADE)


class PillowsLike(LikeCommon):
    post = models.ForeignKey(Pillows, on_delete=models.CASCADE)


class TensorflowsLike(LikeCommon):
    post = models.ForeignKey(Tensorflows, on_delete=models.CASCADE)


class DSPythonLike(LikeCommon):
    post = models.ForeignKey(DSPython, on_delete=models.CASCADE)
