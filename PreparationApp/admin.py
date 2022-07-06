from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin

# Register your models here.


class AptitudeAdmin(CommonAdmin):
    model = Aptitude


class ReasoningAdmin(CommonAdmin):
    model = Reasoning


class VerbalAbilityAdmin(CommonAdmin):
    model = VerbalAbility


class InterviewQuestionAdmin(CommonAdmin):
    model = InterviewQuestion


class CompanyQuestionAdmin(CommonAdmin):
    model = CompanyQuestion


# parent Admin
@admin.register(AptitudeParent)
class AptitudeParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AptitudeAdmin,)


@admin.register(ReasoningParent)
class ReasoningParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ReasoningAdmin,)


@admin.register(VerbalAbilityParent)
class VerbalAbilityParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (VerbalAbilityAdmin,)


@admin.register(InterviewQuestionParent)
class InterviewQuestionParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (InterviewQuestionAdmin,)


@admin.register(CompanyQuestionParent)
class CompanyQuestionParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CompanyQuestionAdmin,)
