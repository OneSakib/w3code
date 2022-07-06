from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin


# Register your models here.

class ServletsAdmin(CommonAdmin):
    model = Servlets


class JSPsAdmin(CommonAdmin):
    model = JSPs


class SpringBootAdmin(CommonAdmin):
    model = SpringBoot


class SpringFrameworkAdmin(CommonAdmin):
    model = SpringFramework


class HibernatesAdmin(CommonAdmin):
    model = Hibernates


class JavaSwingsAdmin(CommonAdmin):
    model = JavaSwings


class JavaFXsAdmin(CommonAdmin):
    model = JavaFXs


class JavaAWTAdmin(CommonAdmin):
    model = JavaAWT


class CollectionsAdmin(CommonAdmin):
    model = Collections


class JavaDateAdmin(CommonAdmin):
    model = JavaDate


class JavaIOAdmin(CommonAdmin):
    model = JavaIO


# Parent Admin

@admin.register(ServletsParent)
class ServletsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ServletsAdmin,)


@admin.register(JSPsParent)
class JSPsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JSPsAdmin,)


@admin.register(SpringBootParent)
class SpringBootParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SpringBootAdmin,)


@admin.register(SpringFrameworkParent)
class SpringFrameworkParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SpringFrameworkAdmin,)


@admin.register(HibernatesParent)
class HibernatesParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (HibernatesAdmin,)


@admin.register(JavaSwingsParent)
class JavaSwingsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaSwingsAdmin,)


@admin.register(JavaFXsParent)
class JavaFXsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaFXsAdmin,)


@admin.register(JavaAWTParent)
class JavaAWTParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaAWTAdmin,)


@admin.register(CollectionsParent)
class CollectionsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CollectionsAdmin,)


@admin.register(JavaDateParent)
class JavaDateParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaDateAdmin,)


@admin.register(JavaIOParent)
class JavaIOParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (JavaIOAdmin,)
