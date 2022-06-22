from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(HTMLs)
class HTMLsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(CSSs)
class CSSsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Laravels)
class LaravelsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Wordpress)
class WordpressAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(JSONs)
class JSONsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Ajaxs)
class AjaxsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Bootstraps)
class BootstrapsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}




# Comments
@admin.register(HTMLsComments)
class HTMLsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(CSSsComments)
class CSSsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(LaravelsComments)
class LaravelsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(WordpressComments)
class WordpressCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JSONsComments)
class JSONsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(AjaxsComments)
class AjaxsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(BootstrapsComments)
class BootstrapsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


