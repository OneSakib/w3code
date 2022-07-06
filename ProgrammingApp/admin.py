from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.

class CLanguageAdmin(CommonAdmin):
    model = CLanguage


class CplusLanguageAdmin(CommonAdmin):
    model = CplusLanguage


class PythonLanguageAdmin(CommonAdmin):
    model = PythonLanguage


class JavaLanguageAdmin(CommonAdmin):
    model = JavaLanguage


class AndroidLanguageAdmin(CommonAdmin):
    model = AndroidLanguage


class KotlinLanguageAdmin(CommonAdmin):
    model = KotlinLanguage


class RLanguageAdmin(CommonAdmin):
    model = RLanguage


class CsharpLanguageAdmin(CommonAdmin):
    model = CsharpLanguage


class SwiftLanguageAdmin(CommonAdmin):
    model = SwiftLanguage


class JavaScriptAdmin(CommonAdmin):
    model = JavaScriptLanguage


class PHPLanguageAdmin(CommonAdmin):
    model = PHPLanguage


class DotNetLanguageAdmin(CommonAdmin):
    model = DotNetLanguage


# Parent Admin
@admin.register(CLanguageParent)
class CLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CLanguageAdmin,)


@admin.register(CplusLanguageParent)
class CplusLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CplusLanguageAdmin,)


@admin.register(PythonLanguageParent)
class PythonLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PythonLanguageAdmin,)


@admin.register(JavaLanguageParent)
class JavaLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaLanguageAdmin,)


@admin.register(AndroidLanguageParent)
class AndroidLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AndroidLanguageAdmin,)


@admin.register(KotlinLanguageParent)
class KotlinLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (KotlinLanguageAdmin,)


@admin.register(RLanguageParent)
class RLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (RLanguageAdmin,)


@admin.register(CsharpLanguageParent)
class CsharpLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CsharpLanguageAdmin,)


@admin.register(SwiftLanguageParent)
class SwiftLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SwiftLanguageAdmin,)


@admin.register(JavaScriptLanguageParent)
class JavaScriptLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaScriptAdmin,)


@admin.register(PHPLanguageParent)
class PHPLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PHPLanguageAdmin,)


@admin.register(DotNetLanguageParent)
class DotNetLanguageParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DotNetLanguageAdmin,)
