from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(MSExcel)
class MSExcelAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MSWord)
class MSWordAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MSPowerpoint)
class MSPowerpointAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MSOneNote)
class MSOneNoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin
@admin.register(MSExcelParent)
class MSExcelParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MSWordParent)
class MSWordParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MSPowerpointParent)
class MSPowerpointParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MSOneNoteParent)
class MSOneNoteParentAdmin(admin.ModelAdmin):
    list_display = ['title']
