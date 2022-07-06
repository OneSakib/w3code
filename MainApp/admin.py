from django.contrib import admin
from .models import *


# Register your models here.
# Child


class CommonAdmin(admin.StackedInline):
    extra = 1
    prepopulated_fields = {'slug': ['title']}


@admin.register(TutList)
class TutListAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    filter = ['type']


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(ArticleBookmark)
