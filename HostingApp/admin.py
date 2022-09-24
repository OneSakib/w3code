from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(DigitalOcean)
class DigitalOceanAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AWS)
class AWSAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PythonAnywhere)
class PythonAnywhereAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(HerokuApp)
class HerokuAppAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(GithubHost)
class GithubHostAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(BlueHost)
class BlueHostAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(HostGator)
class HostGatorAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(InMotionHosting)
class InMotionHostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(A2Hosting)
class A2HostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(GreenGeeks)
class GreenGeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Hostinger)
class HostingerAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MSAzure)
class MSAzureAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(GoDaddy)
class GoDaddyAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# parent
@admin.register(DigitalOceanParent)
class DigitalOceanParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MSAzureParent)
class MSAzureParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AWSParent)
class AWSParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PythonAnywhereParent)
class PythonAnywhereParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(HerokuAppParent)
class HerokuAppParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GithubHostParent)
class GithubHostParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(BlueHostParent)
class BlueHostParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(HostGatorParent)
class HostGatorParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(InMotionHostingParent)
class InMotionHostingParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(A2HostingParent)
class A2HostingParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GreenGeeksParent)
class GreenGeeksParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(HostingerParent)
class HostingerParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GoDaddyParent)
class GoDaddyParentAdmin(admin.ModelAdmin):
    list_display = ['title']
