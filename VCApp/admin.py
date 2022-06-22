from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Docker)
class DockerAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Gits)
class GitsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Githubs)
class GithubsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(GitsComments)
class GitsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(DockerComments)
class DockerCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(GithubsComments)
class GithubsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
