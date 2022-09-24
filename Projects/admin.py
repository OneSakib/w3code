from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(CProjects)
class CProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CPlusProjects)
class CPlusProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonProjects)
class PythonProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaProjects)
class JavaProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(KotlinProjects)
class KotlinProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RProjects)
class RProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CSharpProjects)
class CSharpProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SwiftProjects)
class SwiftProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaScriptProjects)
class JavaScriptProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AndroidProjects)
class AndroidProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PHPProjects)
class PHPProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DotNetProjects)
class DotNetProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin
@admin.register(CProjectsParent)
class CProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CPlusProjectsParent)
class CPlusProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PythonProjectsParent)
class PythonProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaProjectsParent)
class JavaProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(KotlinProjectsParent)
class KotlinProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(RProjectsParent)
class RProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CSharpProjectsParent)
class CSharpProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SwiftProjectsParent)
class SwiftProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaScriptProjectsParent)
class JavaScriptProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AndroidProjectsParent)
class AndroidProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PHPProjectsParent)
class PHPProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DotNetProjectsParent)
class DotNetProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
