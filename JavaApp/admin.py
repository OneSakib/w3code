from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Servlets)
class ServletsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JSPs)
class JSPsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SpringBoot)
class SpringBootAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SpringFramework)
class SpringFrameworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Hibernates)
class HibernatesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaSwings)
class JavaSwingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaFXs)
class JavaFXsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaAWT)
class JavaAWTAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaDate)
class JavaDateAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(JavaIO)
class JavaIOAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(ServletsComments)
class ServletsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JSPsComments)
class JSPsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(SpringBootComments)
class SpringBootCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(SpringFrameworkComments)
class SpringFrameworkCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(HibernatesComments)
class HibernatesCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JavaSwingsComments)
class JavaSwingsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JavaFXsComments)
class JavaFXsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JavaAWTComments)
class JavaAWTCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(CollectionsComments)
class CollectionsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JavaDateComments)
class JavaDateCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(JavaIOComments)
class JavaIOCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
