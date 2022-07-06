from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin

# Register your models here.



class CProgrammeAdmin(CommonAdmin):
    model = CProgramme


class CPlusProgrammeAdmin(CommonAdmin):
    model = CPlusProgramme


class PythonProgrammeAdmin(CommonAdmin):
    model = PythonProgramme


class JavaProgrammeAdmin(CommonAdmin):
    model = JavaProgramme


class KotlinProgrammeAdmin(CommonAdmin):
    model = KotlinProgramme


class RProgrammeAdmin(CommonAdmin):
    model = RProgramme


class CSharpProgrammeAdmin(CommonAdmin):
    model = CSharpProgramme


class SwiftProgrammeAdmin(CommonAdmin):
    model = SwiftProgramme


class JavaScriptProgrammeAdmin(CommonAdmin):
    model = JavaScriptProgramme


class PHPProgrammeAdmin(CommonAdmin):
    model = PHPProgramme


class DotNetProgrammeAdmin(CommonAdmin):
    model = DotNetProgramme


# Parent Admin

@admin.register(CProgrammeParent)
class CProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CProgrammeAdmin,)


@admin.register(CPlusProgrammeParent)
class CPlusProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CPlusProgrammeAdmin,)


@admin.register(PythonProgrammeParent)
class PythonProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PythonProgrammeAdmin,)


@admin.register(JavaProgrammeParent)
class JavaProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaProgrammeAdmin,)


@admin.register(KotlinProgrammeParent)
class KotlinProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (KotlinProgrammeAdmin,)


@admin.register(RProgrammeParent)
class RProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (RProgrammeAdmin,)


@admin.register(CSharpProgrammeParent)
class CSharpProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CSharpProgrammeAdmin,)


@admin.register(SwiftProgrammeParent)
class SwiftProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SwiftProgrammeAdmin,)


@admin.register(JavaScriptProgrammeParent)
class JavaScriptProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaScriptProgrammeAdmin,)


@admin.register(PHPProgrammeParent)
class PHPProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PHPProgrammeAdmin,)


@admin.register(DotNetProgrammeParent)
class DotNetProgrammeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DotNetProgrammeAdmin,)
