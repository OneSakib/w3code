from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.


class DigitalOceanAdmin(CommonAdmin):
    model = DigitalOcean


class AWSAdmin(CommonAdmin):
    model = AWS


class PythonAnywhereAdmin(CommonAdmin):
    model = PythonAnywhere


class HerokuAppAdmin(CommonAdmin):
    model = HerokuApp


class GithubHostAdmin(CommonAdmin):
    model = GithubHost


class BlueHostAdmin(CommonAdmin):
    model = BlueHost


class HostGatorAdmin(CommonAdmin):
    model = HostGator


class InMotionHostingAdmin(CommonAdmin):
    model = InMotionHosting


class A2HostingAdmin(CommonAdmin):
    model = A2Hosting


class GreenGeeksAdmin(CommonAdmin):
    model = GreenGeeks


class HostingerAdmin(CommonAdmin):
    model = Hostinger


class MSAzureAdmin(CommonAdmin):
    model = MSAzure


class GoDaddyAdmin(CommonAdmin):
    model = GoDaddy


# parent
@admin.register(DigitalOceanParent)
class DigitalOceanParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DigitalOceanAdmin,)


@admin.register(MSAzureParent)
class MSAzureParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MSAzureAdmin,)


@admin.register(AWSParent)
class AWSParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AWSAdmin,)


@admin.register(PythonAnywhereParent)
class PythonAnywhereParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PythonAnywhereAdmin,)


@admin.register(HerokuAppParent)
class HerokuAppParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (HerokuAppAdmin,)


@admin.register(GithubHostParent)
class GithubHostParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (GithubHostAdmin,)


@admin.register(BlueHostParent)
class BlueHostParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (BlueHostAdmin,)


@admin.register(HostGatorParent)
class HostGatorParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (HostGatorAdmin,)


@admin.register(InMotionHostingParent)
class InMotionHostingParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (InMotionHostingAdmin,)


@admin.register(A2HostingParent)
class A2HostingParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (A2HostingAdmin,)


@admin.register(GreenGeeksParent)
class GreenGeeksParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (GreenGeeksAdmin,)


@admin.register(HostingerParent)
class HostingerParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (HostingerAdmin,)


@admin.register(GoDaddyParent)
class GoDaddyParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (GoDaddyAdmin,)
