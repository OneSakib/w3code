from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Django)
class DjangoAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Flask)
class FlaskAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(MachineLearning)
class MachineLearningAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Numpys)
class NumpysAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Tkinters)
class TkintersAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Pytorchs)
class PytorchsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Pygames)
class PygamesAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Scipys)
class ScipysAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Pandass)
class PandassAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(OpenCVs)
class OpenCVsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Matplotlibs)
class MatplotlibsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Seleniums)
class SeleniumsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Kivys)
class KivysAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Jupyters)
class JupytersAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(DataScience)
class DataScienceAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(DeepLearning)
class DeepLearningAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Pillows)
class PillowsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Tensorflows)
class TensorflowsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


# comments
@admin.register(DjangoComments)
class DjangoCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(FlaskComments)
class FlaskCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(MachineLearningComments)
class MachineLearningCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(NumpysComments)
class NumpysCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(TkintersComments)
class TkintersCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(PytorchsComments)
class PytorchsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(PygamesComments)
class PygamesCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(ScipysComments)
class ScipysCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(PandassComments)
class PandassCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(OpenCVsComments)
class OpenCVsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(MatplotlibsComments)
class MatplotlibsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(SeleniumsComments)
class SeleniumsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(KivysComments)
class KivysCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(JupytersComments)
class JupytersCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(DataScienceComments)
class DataScienceCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(DeepLearningComments)
class DeepLearningCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(PillowsComments)
class PillowsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(TensorflowsComments)
class TensorflowsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
