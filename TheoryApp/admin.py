from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(DBMS)
class DBMSAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DataStructure)
class DataStructureAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DAA)
class DAAAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(ComputerNetwork)
class ComputerNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CompilerDesign)
class CompilerDesignAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(ComputerOrganization)
class ComputerOrganizationAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DiscreteMathematics)
class DiscreteMathematicsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SoftwareEngineering)
class SoftwareEngineeringAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(CyberSecurity)
class CyberSecurityAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DataMining)
class DataMiningAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(ArtificialIntelligence)
class ArtificialIntelligenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Automata)
class AutomataAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(ComputerGraphics)
class ComputerGraphicsAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(WebApi)
class WebApiAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DDBMS)
class DDBMSAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# ADmin Parent
@admin.register(DBMSParent)
class DBMSParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DataStructureParent)
class DataStructureParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DAAParent)
class DAAParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(OperatingSystemParent)
class OperatingSystemParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ComputerNetworkParent)
class ComputerNetworkParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CompilerDesignParent)
class CompilerDesignParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ComputerOrganizationParent)
class ComputerOrganizationParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DiscreteMathematicsParent)
class DiscreteMathematicsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SoftwareEngineeringParent)
class SoftwareEngineeringParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CyberSecurityParent)
class CyberSecurityParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DataMiningParent)
class DataMiningParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ArtificialIntelligenceParent)
class ArtificialIntelligenceParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AutomataParent)
class AutomataParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ComputerGraphicsParent)
class ComputerGraphicsParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(WebApiParent)
class WebApiParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DDBMSParent)
class DDBMSParentAdmin(admin.ModelAdmin):
    list_display = ['title']
