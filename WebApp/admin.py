from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(HTMLs)
class HTMLsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CSSs)
class CSSsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Laravels)
class LaravelsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Wordpress)
class WordpressAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JSONs)
class JSONsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Ajaxs)
class AjaxsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Bootstraps)
class BootstrapsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Admin Parent
@admin.register(HTMLsParent)
class HTMLsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CSSsParent)
class CSSsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(LaravelsParent)
class LaravelsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(WordpressParent)
class WordpressParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JSONsParent)
class JSONsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AjaxsParent)
class AjaxsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(BootstrapsParent)
class BootstrapsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
