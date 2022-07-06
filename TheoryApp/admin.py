from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin

# Register your models here.




class DBMSAdmin(CommonAdmin):
    model = DBMS


class DataStructureAdmin(CommonAdmin):
    model = DataStructure


class DAAAdmin(CommonAdmin):
    model = DAA


class OperatingSystemAdmin(CommonAdmin):
    model = OperatingSystem


class ComputerNetworkAdmin(CommonAdmin):
    model = ComputerNetwork


class CompilerDesignAdmin(CommonAdmin):
    model = CompilerDesign


class ComputerOrganizationAdmin(CommonAdmin):
    model = ComputerOrganization


class DiscreteMathematicsAdmin(CommonAdmin):
    model = DiscreteMathematics


class SoftwareEngineeringAdmin(CommonAdmin):
    model = SoftwareEngineering


class CyberSecurityAdmin(CommonAdmin):
    model = CyberSecurity


class DataMiningAdmin(CommonAdmin):
    model = DataMining


class ArtificialIntelligenceAdmin(CommonAdmin):
    model = ArtificialIntelligence


class AutomataAdmin(CommonAdmin):
    model = Automata


class ComputerGraphicsAdmin(CommonAdmin):
    model = ComputerGraphics


class WebApiAdmin(CommonAdmin):
    model = WebApi


class DDBMSAdmin(CommonAdmin):
    model = DDBMS


# ADmin Parent
@admin.register(DBMSParent)
class DBMSParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DBMSAdmin,)


@admin.register(DataStructureParent)
class DataStructureParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DataStructureAdmin,)


@admin.register(DAAParent)
class DAAParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DAAAdmin,)


@admin.register(OperatingSystemParent)
class OperatingSystemParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (OperatingSystemAdmin,)


@admin.register(ComputerNetworkParent)
class ComputerNetworkParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ComputerNetworkAdmin,)


@admin.register(CompilerDesignParent)
class CompilerDesignParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CompilerDesignAdmin,)


@admin.register(ComputerOrganizationParent)
class ComputerOrganizationParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ComputerOrganizationAdmin,)


@admin.register(DiscreteMathematicsParent)
class DiscreteMathematicsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DiscreteMathematicsAdmin,)


@admin.register(SoftwareEngineeringParent)
class SoftwareEngineeringParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SoftwareEngineeringAdmin,)


@admin.register(CyberSecurityParent)
class CyberSecurityParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (CyberSecurityAdmin,)


@admin.register(DataMiningParent)
class DataMiningParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DataMiningAdmin,)


@admin.register(ArtificialIntelligenceParent)
class ArtificialIntelligenceParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ArtificialIntelligenceAdmin,)


@admin.register(AutomataParent)
class AutomataParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (AutomataAdmin,)


@admin.register(ComputerGraphicsParent)
class ComputerGraphicsParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (ComputerGraphicsAdmin,)


@admin.register(WebApiParent)
class WebApiParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (WebApiAdmin,)


@admin.register(DDBMSParent)
class DDBMSParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (DDBMSAdmin,)
