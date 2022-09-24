from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(CProgramme)
class CProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CPlusProgramme)
class CPlusProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonProgramme)
class PythonProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaProgramme)
class JavaProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(KotlinProgramme)
class KotlinProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RProgramme)
class RProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CSharpProgramme)
class CSharpProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SwiftProgramme)
class SwiftProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaScriptProgramme)
class JavaScriptProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PHPProgramme)
class PHPProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DotNetProgramme)
class DotNetProgrammeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin

@admin.register(CProgrammeParent)
class CProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CPlusProgrammeParent)
class CPlusProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PythonProgrammeParent)
class PythonProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaProgrammeParent)
class JavaProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(KotlinProgrammeParent)
class KotlinProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(RProgrammeParent)
class RProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CSharpProgrammeParent)
class CSharpProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SwiftProgrammeParent)
class SwiftProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaScriptProgrammeParent)
class JavaScriptProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PHPProgrammeParent)
class PHPProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DotNetProgrammeParent)
class DotNetProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
