from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Docker)
class DockerAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Gits)
class GitsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Githubs)
class GithubsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin
@admin.register(DockerParent)
class DockerParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GitsParent)
class GitsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GithubsParent)
class GithubsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
