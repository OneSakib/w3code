from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Aptitude)
class AptitudeAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Reasoning)
class ReasoningAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(VerbalAbility)
class VerbalAbilityAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CompanyQuestion)
class CompanyQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# parent Admin
@admin.register(AptitudeParent)
class AptitudeParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ReasoningParent)
class ReasoningParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(VerbalAbilityParent)
class VerbalAbilityParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(InterviewQuestionParent)
class InterviewQuestionParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CompanyQuestionParent)
class CompanyQuestionParentAdmin(admin.ModelAdmin):
    list_display = ['title']
