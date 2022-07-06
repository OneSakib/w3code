from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.

class JqueryAdmin(CommonAdmin):
    model = Jquery


class AngularjsAdmin(CommonAdmin):
    model = Angularjs


class NodejsAdmin(CommonAdmin):
    model = Nodejs


class ExpressjsAdmin(CommonAdmin):
    model = Expressjs


class ReactjsAdmin(CommonAdmin):
    model = Reactjs


class TypeScriptsAdmin(CommonAdmin):
    model = TypeScripts


class VUEjsAdmin(CommonAdmin):
    model = VUEjs


# Parent Admin

@admin.register(JqueryParent)
class JqueryParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JqueryAdmin,)


@admin.register(AngularjsParent)
class AngularjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AngularjsAdmin,)


@admin.register(NodejsParent)
class NodejsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (NodejsAdmin,)


@admin.register(ExpressjsParent)
class ExpressjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ExpressjsAdmin,)


@admin.register(ReactjsParent)
class ReactjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ReactjsAdmin,)


@admin.register(TypeScriptsParent)
class TypeScriptsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (TypeScriptsAdmin,)


@admin.register(VUEjsParent)
class VUEjsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (VUEjsAdmin,)
