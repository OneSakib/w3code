from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(CLanguage)
class CLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CplusLanguage)
class CplusLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonLanguage)
class PythonLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaLanguage)
class JavaLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AndroidLanguage)
class AndroidLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(KotlinLanguage)
class KotlinLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RLanguage)
class RLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CsharpLanguage)
class CsharpLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SwiftLanguage)
class SwiftLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PHPLanguage)
class PHPLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


# Comments

@admin.register(CLanguageComments)
class CLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(CplusLanguageComments)
class CplusLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(PythonLanguageComments)
class PythonLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(JavaLanguageComments)
class JavaLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(AndroidLanguageComments)
class AndroidLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(KotlinLanguageComments)
class KotlinLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(RLanguageComments)
class RLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(CsharpLanguageComments)
class CsharpLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(SwiftLanguageComments)
class SwiftLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(JavaScriptLanguageComments)
class JavaScriptLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(PHPLanguageComments)
class PHPLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(DotNetLanguageComments)
class DotNetLanguageCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
