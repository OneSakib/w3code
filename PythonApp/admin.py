from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.



class DjangoAdmin(CommonAdmin):
    model = Django


class RestApiAdmin(CommonAdmin):
    model = RestApi


class FlaskAdmin(CommonAdmin):
    model = Flask


class MachineLearningAdmin(CommonAdmin):
    model = MachineLearning


class NumpysAdmin(CommonAdmin):
    model = Numpys


class TkintersAdmin(CommonAdmin):
    model = Tkinters


class PytorchsAdmin(CommonAdmin):
    model = Pytorchs


class PygamesAdmin(CommonAdmin):
    model = Pygames


class ScipysAdmin(CommonAdmin):
    model = Scipys


class PandassAdmin(CommonAdmin):
    model = Pandass


class OpenCVsAdmin(CommonAdmin):
    model = OpenCVs


class MatplotlibsAdmin(CommonAdmin):
    model = Matplotlibs


class SeleniumsAdmin(CommonAdmin):
    model = Seleniums


class KivysAdmin(CommonAdmin):
    model = Kivys


class JupytersAdmin(CommonAdmin):
    model = Jupyters


class DataScienceAdmin(CommonAdmin):
    model = DataScience


class DeepLearningAdmin(CommonAdmin):
    model = DeepLearning


class PillowsAdmin(CommonAdmin):
    model = Pillows


class TensorflowsAdmin(CommonAdmin):
    model = Tensorflows


class DSPythonAdmin(CommonAdmin):
    model = DSPython


# Parent ADmin
@admin.register(DjangoParent)
class DjangoParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DjangoAdmin,)


@admin.register(RestApiParent)
class RestApiParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (RestApiAdmin,)


@admin.register(FlaskParent)
class FlaskParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (FlaskAdmin,)


@admin.register(MachineLearningParent)
class MachineLearningParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MachineLearningAdmin,)


@admin.register(NumpysParent)
class NumpysParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (NumpysAdmin,)


@admin.register(TkintersParent)
class TkintersParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (TkintersAdmin,)


@admin.register(PytorchsParent)
class PytorchsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PytorchsAdmin,)


@admin.register(PygamesParent)
class PygamesParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PygamesAdmin,)


@admin.register(ScipysParent)
class ScipysParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ScipysAdmin,)


@admin.register(PandassParent)
class PandassParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PandassAdmin,)


@admin.register(OpenCVsParent)
class OpenCVsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (OpenCVsAdmin,)


@admin.register(MatplotlibsParent)
class MatplotlibsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MatplotlibsAdmin,)


@admin.register(SeleniumsParent)
class SeleniumsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SeleniumsAdmin,)


@admin.register(KivysParent)
class KivysParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (KivysAdmin,)


@admin.register(JupytersParent)
class JupytersParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JupytersAdmin,)


@admin.register(DataScienceParent)
class DataScienceParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DataScienceAdmin,)


@admin.register(DeepLearningParent)
class DeepLearningParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DeepLearningAdmin,)


@admin.register(PillowsParent)
class PillowsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PillowsAdmin,)


@admin.register(TensorflowsParent)
class TensorflowsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (TensorflowsAdmin,)


@admin.register(DSPythonParent)
class DSPythonParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DSPythonAdmin,)
