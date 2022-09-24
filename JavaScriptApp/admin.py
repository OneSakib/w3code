from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Jquery)
class JqueryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Angularjs)
class AngularjsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Nodejs)
class NodejsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Expressjs)
class ExpressjsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Reactjs)
class ReactjsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(TypeScripts)
class TypeScriptsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(VUEjs)
class VUEjsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin

@admin.register(JqueryParent)
class JqueryParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AngularjsParent)
class AngularjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(NodejsParent)
class NodejsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ExpressjsParent)
class ExpressjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ReactjsParent)
class ReactjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(TypeScriptsParent)
class TypeScriptsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(VUEjsParent)
class VUEjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
