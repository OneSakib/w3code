from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Servlets)
class ServletsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JSPs)
class JSPsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SpringBoot)
class SpringBootAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SpringFramework)
class SpringFrameworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Hibernates)
class HibernatesAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaSwings)
class JavaSwingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaFXs)
class JavaFXsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaAWT)
class JavaAWTAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaDate)
class JavaDateAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaIO)
class JavaIOAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# Parent Admin

@admin.register(ServletsParent)
class ServletsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JSPsParent)
class JSPsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SpringBootParent)
class SpringBootParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SpringFrameworkParent)
class SpringFrameworkParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(HibernatesParent)
class HibernatesParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaSwingsParent)
class JavaSwingsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaFXsParent)
class JavaFXsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaAWTParent)
class JavaAWTParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CollectionsParent)
class CollectionsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaDateParent)
class JavaDateParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(JavaIOParent)
class JavaIOParentAdmin(admin.ModelAdmin):
    list_display = ['title']
