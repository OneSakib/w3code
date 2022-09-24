from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Django)
class DjangoAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RestApi)
class RestApiAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Flask)
class FlaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MachineLearning)
class MachineLearningAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Numpys)
class NumpysAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Tkinters)
class TkintersAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Pytorchs)
class PytorchsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Pygames)
class PygamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Scipys)
class ScipysAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Pandass)
class PandassAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(OpenCVs)
class OpenCVsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Matplotlibs)
class MatplotlibsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Seleniums)
class SeleniumsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Kivys)
class KivysAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Jupyters)
class JupytersAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DataScience)
class DataScienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DeepLearning)
class DeepLearningAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Pillows)
class PillowsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Tensorflows)
class TensorflowsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DSPython)
class DSPythonAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent ADmin
@admin.register(DjangoParent)
class DjangoParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(RestApiParent)
class RestApiParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(FlaskParent)
class FlaskParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MachineLearningParent)
class MachineLearningParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(NumpysParent)
class NumpysParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(TkintersParent)
class TkintersParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PytorchsParent)
class PytorchsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PygamesParent)
class PygamesParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ScipysParent)
class ScipysParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PandassParent)
class PandassParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(OpenCVsParent)
class OpenCVsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MatplotlibsParent)
class MatplotlibsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SeleniumsParent)
class SeleniumsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(KivysParent)
class KivysParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JupytersParent)
class JupytersParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DataScienceParent)
class DataScienceParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DeepLearningParent)
class DeepLearningParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PillowsParent)
class PillowsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(TensorflowsParent)
class TensorflowsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DSPythonParent)
class DSPythonParentAdmin(admin.ModelAdmin):
    list_display = ['title']
