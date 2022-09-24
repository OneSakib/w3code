from django.contrib import admin
from .models import *

# Register your models here.
# Child

admin.site.register(EmailVerification)




@admin.register(TutList)
class TutListAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    filter = ['type']


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(ArticleBookmark)


# Profile Image
@admin.register(ProfileImage)
class ProfleImageAdmin(admin.ModelAdmin):
    list_display = ['user']


# Author Profile
@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user']
