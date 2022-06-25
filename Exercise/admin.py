from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(CExercise)
class CExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CPlusExercise)
class CPlusExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonExercise)
class PythonExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaExercise)
class JavaExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(KotlinExercise)
class KotlinExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(RExercise)
class RExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CSharpExercise)
class CSharpExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SwiftExercise)
class SwiftExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaScriptExercise)
class JavaScriptExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PHPExercise)
class PHPExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DotNetExercise)
class DotNetExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


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
