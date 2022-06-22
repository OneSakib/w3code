from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Jquery)
class JqueryAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Angularjs)
class AngularjsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Nodejs)
class NodejsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Expressjs)
class ExpressjsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Reactjs)
class ReactjsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(TypeScripts)
class TypeScriptsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(VUEjs)
class VUEjsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(JqueryComments)
class JqueryCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(AngularjsComments)
class AngularjsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(NodejsComments)
class NodejsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ExpressjsComments)
class ExpressjsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ReactjsComments)
class ReactjsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(TypeScriptsComments)
class TypeScriptsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(VUEjsComments)
class VUEjsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


