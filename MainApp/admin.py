from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(TutList)
class TutListAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    filter = ['type']

