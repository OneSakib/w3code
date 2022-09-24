from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CLanguage)
class CLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CplusLanguage)
class CplusLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonLanguage)
class PythonLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaLanguage)
class JavaLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AndroidLanguage)
class AndroidLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(KotlinLanguage)
class KotlinLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RLanguage)
class RLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CsharpLanguage)
class CsharpLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SwiftLanguage)
class SwiftLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaScriptLanguage)
class JavaScriptAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PHPLanguage)
class PHPLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DotNetLanguage)
class DotNetLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin
@admin.register(CLanguageParent)
class CLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CplusLanguageParent)
class CplusLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PythonLanguageParent)
class PythonLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaLanguageParent)
class JavaLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AndroidLanguageParent)
class AndroidLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(KotlinLanguageParent)
class KotlinLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(RLanguageParent)
class RLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CsharpLanguageParent)
class CsharpLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SwiftLanguageParent)
class SwiftLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaScriptLanguageParent)
class JavaScriptLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PHPLanguageParent)
class PHPLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DotNetLanguageParent)
class DotNetLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
