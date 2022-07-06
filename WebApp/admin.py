from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.


class HTMLsAdmin(CommonAdmin):
    model = HTMLs


class CSSsAdmin(CommonAdmin):
    model = CSSs


class LaravelsAdmin(CommonAdmin):
    model = Laravels


class WordpressAdmin(CommonAdmin):
    model = Wordpress


class JSONsAdmin(CommonAdmin):
    model = JSONs


class AjaxsAdmin(CommonAdmin):
    model = Ajaxs


class BootstrapsAdmin(CommonAdmin):
    model = Bootstraps


# Admin Parent
@admin.register(HTMLsParent)
class HTMLsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (HTMLsAdmin,)


@admin.register(CSSsParent)
class CSSsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CSSsAdmin,)


@admin.register(LaravelsParent)
class LaravelsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (LaravelsAdmin,)


@admin.register(WordpressParent)
class WordpressParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (WordpressAdmin,)


@admin.register(JSONsParent)
class JSONsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JSONsAdmin,)


@admin.register(AjaxsParent)
class AjaxsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AjaxsAdmin,)


@admin.register(BootstrapsParent)
class BootstrapsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (BootstrapsAdmin,)
