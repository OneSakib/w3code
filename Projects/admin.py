from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.


class CProjectsAdmin(CommonAdmin):
    model = CProjects


class CPlusProjectsAdmin(CommonAdmin):
    model = CPlusProjects


class PythonProjectsAdmin(CommonAdmin):
    model = PythonProjects


class JavaProjectsAdmin(CommonAdmin):
    model = JavaProjects


class KotlinProjectsAdmin(CommonAdmin):
    model = KotlinProjects


class RProjectsAdmin(CommonAdmin):
    model = RProjects


class CSharpProjectsAdmin(CommonAdmin):
    model = CSharpProjects


class SwiftProjectsAdmin(CommonAdmin):
    model = SwiftProjects


class JavaScriptProjectsAdmin(CommonAdmin):
    model = JavaScriptProjects


class AndroidProjectsAdmin(CommonAdmin):
    model = AndroidProjects


class PHPProjectsAdmin(CommonAdmin):
    model = PHPProjects


class DotNetProjectsAdmin(CommonAdmin):
    model = DotNetProjects


# Parent Admin
@admin.register(CProjectsParent)
class CProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CProjectsAdmin,)


@admin.register(CPlusProjectsParent)
class CPlusProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CPlusProjectsAdmin,)


@admin.register(PythonProjectsParent)
class PythonProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PythonProjectsAdmin,)


@admin.register(JavaProjectsParent)
class JavaProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaProjectsAdmin,)


@admin.register(KotlinProjectsParent)
class KotlinProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (KotlinProjectsAdmin,)


@admin.register(RProjectsParent)
class RProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (RProjectsAdmin,)


@admin.register(CSharpProjectsParent)
class CSharpProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CSharpProjectsAdmin,)


@admin.register(SwiftProjectsParent)
class SwiftProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SwiftProjectsAdmin,)


@admin.register(JavaScriptProjectsParent)
class JavaScriptProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaScriptProjectsAdmin,)


@admin.register(AndroidProjectsParent)
class AndroidProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AndroidProjectsAdmin,)


@admin.register(PHPProjectsParent)
class PHPProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PHPProjectsAdmin,)


@admin.register(DotNetProjectsParent)
class DotNetProjectsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DotNetProjectsAdmin,)
