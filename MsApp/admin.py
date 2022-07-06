from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.

class MSExcelAdmin(CommonAdmin):
    model = MSExcel


class MSWordAdmin(CommonAdmin):
    model = MSWord


class MSPowerpointAdmin(CommonAdmin):
    model = MSPowerpoint


class MSOneNoteAdmin(CommonAdmin):
    model = MSOneNote


# Parent Admin
@admin.register(MSExcelParent)
class MSExcelParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MSExcelAdmin,)


@admin.register(MSWordParent)
class MSWordParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MSWordAdmin,)


@admin.register(MSPowerpointParent)
class MSPowerpointParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MSPowerpointAdmin,)


@admin.register(MSOneNoteParent)
class MSOneNoteParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MSOneNoteAdmin,)
