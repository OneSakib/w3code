from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CExercise)
class CExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CPlusExercise)
class CPlusExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonExercise)
class PythonExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaExercise)
class JavaExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(KotlinExercise)
class KotlinExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RExercise)
class RExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CSharpExercise)
class CSharpExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SwiftExercise)
class SwiftExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaScriptExercise)
class JavaScriptExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PHPExercise)
class PHPExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DotNetExercise)
class DotNetExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin register
@admin.register(CExerciseParent)
class CExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CPlusExerciseParent)
class CPlusExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PythonExerciseParent)
class PythonExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaExerciseParent)
class JavaExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(KotlinExerciseParent)
class KotlinExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(RExerciseParent)
class RExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CSharpExerciseParent)
class CSharpExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SwiftExerciseParent)
class SwiftExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaScriptExerciseParent)
class JavaScriptExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PHPExerciseParent)
class PHPExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DotNetExerciseParent)
class DotNetExerciseParentAdmin(admin.ModelAdmin):
    list_display = ['title']
