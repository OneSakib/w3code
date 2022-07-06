from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.


class DockerAdmin(CommonAdmin):
    model = Docker


class GitsAdmin(CommonAdmin):
    model = Gits


class GithubsAdmin(CommonAdmin):
    model = Githubs


# Parent Admin
@admin.register(DockerParent)
class DockerParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DockerAdmin,)


@admin.register(GitsParent)
class GitsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (GitsAdmin,)


@admin.register(GithubsParent)
class GithubsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (GithubsAdmin,)
