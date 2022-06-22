from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Aptitude)
class AptitudeAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Reasoning)
class ReasoningAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(VerbalAbility)
class VerbalAbilityAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(CompanyQuestion)
class CompanyQuestionAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(AptitudeComments)
class AptitudeCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ReasoningComments)
class ReasoningCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(VerbalAbilityComments)
class VerbalAbilityCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(InterviewQuestionComments)
class InterviewQuestionCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(CompanyQuestionComments)
class CompanyQuestionCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
