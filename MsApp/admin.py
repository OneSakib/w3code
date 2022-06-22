from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(MSExcel)
class MSExcelAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(MSWord)
class MSWordAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(MSPowerpoint)
class MSPowerpointAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(MSOneNote)
class MSOneNoteAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(MSWordComments)
class MSWordCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(MSExcelComments)
class MSExcelCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(MSPowerpointComments)
class MSPowerpointCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(MSOneNoteComments)
class MSOneNoteCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
