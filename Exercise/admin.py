from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin

# Register your models here.
class CExerciseAdmin(CommonAdmin):
    model = CExercise


class CPlusExerciseAdmin(CommonAdmin):
    model = CPlusExercise


class PythonExerciseAdmin(CommonAdmin):
    model = PythonExercise


class JavaExerciseAdmin(CommonAdmin):
    model = JavaExercise


class KotlinExerciseAdmin(CommonAdmin):
    model = KotlinExercise


class RExerciseAdmin(CommonAdmin):
    model = RExercise


class CSharpExerciseAdmin(CommonAdmin):
    model = CSharpExercise


class SwiftExerciseAdmin(CommonAdmin):
    model = SwiftExercise


class JavaScriptExerciseAdmin(CommonAdmin):
    model = JavaScriptExercise


class PHPExerciseAdmin(CommonAdmin):
    model = PHPExercise


class DotNetExerciseAdmin(CommonAdmin):
    model = DotNetExercise


# Parent Admin register
@admin.register(CExerciseParent)
class CExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CExerciseAdmin,)


@admin.register(CPlusExerciseParent)
class CPlusExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CPlusExerciseAdmin,)


@admin.register(PythonExerciseParent)
class PythonExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PythonExerciseAdmin,)


@admin.register(JavaExerciseParent)
class JavaExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaExerciseAdmin,)


@admin.register(KotlinExerciseParent)
class KotlinExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (KotlinExerciseAdmin,)


@admin.register(RExerciseParent)
class RExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (RExerciseAdmin,)


@admin.register(CSharpExerciseParent)
class CSharpExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CSharpExerciseAdmin,)


@admin.register(SwiftExerciseParent)
class SwiftExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SwiftExerciseAdmin,)


@admin.register(JavaScriptExerciseParent)
class JavaScriptExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaScriptExerciseAdmin,)


@admin.register(PHPExerciseParent)
class PHPExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PHPExerciseAdmin,)


@admin.register(DotNetExerciseParent)
class DotNetExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DotNetExerciseAdmin,)


admin.site.register(CQuestionAnswer)
admin.site.register(CplusQuestionAnswer)
admin.site.register(CSharpQuestionAnswer)
admin.site.register(JavaQuestionAnswer)
admin.site.register(PythonQuestionAnswer)
admin.site.register(KotlinQuestionAnswer)
admin.site.register(RQuestionAnswer)
admin.site.register(DotNetQuestionAnswer)
admin.site.register(PHPQuestionAnswer)
admin.site.register(SwiftQuestionAnswer)
