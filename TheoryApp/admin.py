from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(DBMS)
class DBMSAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(DataStructure)
class DataStructureAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(DAA)
class DAAAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(ComputerNetwork)
class ComputerNetworkAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(CompilerDesign)
class CompilerDesignAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(ComputerOrganization)
class ComputerOrganizationAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(DiscreteMathematics)
class DiscreteMathematicsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(SoftwareEngineering)
class SoftwareEngineeringAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(CyberSecurity)
class CyberSecurityAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(DataMining)
class DataMiningAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(ArtificialIntelligence)
class ArtificialIntelligenceAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(Automata)
class AutomataAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(ComputerGraphics)
class ComputerGraphicsAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


@admin.register(WebApi)
class WebApiAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(DBMSComments)
class DBMSCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(DataStructureComments)
class DataStructureCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(DAAComments)
class DAACommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(OperatingSystemComments)
class OperatingSystemCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ComputerNetworkComments)
class ComputerNetworkCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(CompilerDesignComments)
class CompilerDesignCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ComputerOrganizationComments)
class ComputerOrganizationCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(DiscreteMathematicsComments)
class DiscreteMathematicsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(SoftwareEngineeringComments)
class SoftwareEngineeringCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(CyberSecurityComments)
class CyberSecurityCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(DataMiningComments)
class DataMiningCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ArtificialIntelligenceComments)
class ArtificialIntelligenceCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(AutomataComments)
class AutomataCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(ComputerGraphicsComments)
class ComputerGraphicsCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(WebApiComments)
class WebApiCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']

