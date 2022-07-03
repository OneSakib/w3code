from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(DigitalOcean)
class DigitalOceanAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AWS)
class AWSAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonAnywhere)
class PythonAnywhereAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(HerokuApp)
class HerokuAppAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(GithubHost)
class GithubHostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(BlueHost)
class BlueHostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(HostGator)
class HostGatorAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(InMotionHosting)
class InMotionHostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(A2Hosting)
class A2HostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(GreenGeeks)
class GreenGeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Hostinger)
class HostingerAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MSAzure)
class MSAzureAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(GoDaddy)
class GoDaddyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


# Comments
# @admin.register(DigitalOceanComments)
# class DigitalOceanCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(MSAzureComments)
# class MSAzureCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(AWSComments)
# class AWSCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(PythonAnywhereComments)
# class PythonAnywhereCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(HerokuAppComments)
# class HerokuAppCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(GithubHostComments)
# class GithubHostCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(BlueHostComments)
# class BlueHostCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(HostGatorComments)
# class HostGatorCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(InMotionHostingComments)
# class InMotionHostingCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(A2HostingComments)
# class A2HostingCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(GreenGeeksComments)
# class GreenGeeksCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(HostingerComments)
# class HostingerCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
#
#
# @admin.register(GoDaddyComments)
# class GoDaddyCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post']
