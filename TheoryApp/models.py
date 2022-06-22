from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Therory Tut
class DBMS(TutCommon):
    class Meta:
        verbose_name_plural = 'DBMS'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:dbmsdetail", kwargs={"slug": self.slug})}'


class DataStructure(TutCommon):
    class Meta:
        verbose_name_plural = 'DataStructure'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:datastructuredetail", kwargs={"slug": self.slug})}'


class DAA(TutCommon):
    class Meta:
        verbose_name_plural = 'DAA'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:daadetail", kwargs={"slug": self.slug})}'


class OperatingSystem(TutCommon):
    class Meta:
        verbose_name_plural = 'OperatingSystem'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:operatingsystemdetail", kwargs={"slug": self.slug})}'


class ComputerNetwork(TutCommon):
    class Meta:
        verbose_name_plural = 'ComputerNetwork'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:computernetworkdetail", kwargs={"slug": self.slug})}'


class CompilerDesign(TutCommon):
    class Meta:
        verbose_name_plural = 'CompilerDesign'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:compilerdesigndetail", kwargs={"slug": self.slug})}'


class ComputerOrganization(TutCommon):
    class Meta:
        verbose_name_plural = 'ComputerOrganization'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:computerorganizationdetail", kwargs={"slug": self.slug})}'


class DiscreteMathematics(TutCommon):
    class Meta:
        verbose_name_plural = 'DiscreteMathematics'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:discretemathematicsdetail", kwargs={"slug": self.slug})}'


class SoftwareEngineering(TutCommon):
    class Meta:
        verbose_name_plural = 'SoftwareEngineering'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:softwareengineeringdetail", kwargs={"slug": self.slug})}'


class CyberSecurity(TutCommon):
    class Meta:
        verbose_name_plural = 'CyberSecurity'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:cybersecuritydetail", kwargs={"slug": self.slug})}'


class DataMining(TutCommon):
    class Meta:
        verbose_name_plural = 'DataMining'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:datamininganddatawarehousedetail", kwargs={"slug": self.slug})}'


class ArtificialIntelligence(TutCommon):
    class Meta:
        verbose_name_plural = 'ArtificialIntelligence'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:artificialintelligencedetail", kwargs={"slug": self.slug})}'


class Automata(TutCommon):
    class Meta:
        verbose_name_plural = 'Automata'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:automatadetail", kwargs={"slug": self.slug})}'


class ComputerGraphics(TutCommon):
    class Meta:
        verbose_name_plural = 'ComputerGraphics'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:computergraphicsdetail", kwargs={"slug": self.slug})}'


class WebApi(TutCommon):
    class Meta:
        verbose_name_plural = 'WebApi'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Theory:webapidetail", kwargs={"slug": self.slug})}'


# Comments
class DBMSComments(Comments):
    post = models.ForeignKey(DBMS, on_delete=models.CASCADE, related_name='DBMSComments')

    class Meta:
        verbose_name_plural = 'DBMSComments'


class DataStructureComments(Comments):
    post = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='DataStructureComments')

    class Meta:
        verbose_name_plural = 'DataStructureComments'


class DAAComments(Comments):
    post = models.ForeignKey(DAA, on_delete=models.CASCADE, related_name='DAAComments')

    class Meta:
        verbose_name_plural = 'DAAComments'


class OperatingSystemComments(Comments):
    post = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE, related_name='OperatingSystemComments')

    class Meta:
        verbose_name_plural = 'OperatingSystemComments'


class ComputerNetworkComments(Comments):
    post = models.ForeignKey(ComputerNetwork, on_delete=models.CASCADE, related_name='ComputerNetworkComments')

    class Meta:
        verbose_name_plural = 'ComputerNetworkComments'


class CompilerDesignComments(Comments):
    post = models.ForeignKey(CompilerDesign, on_delete=models.CASCADE, related_name='CompilerDesignComments')

    class Meta:
        verbose_name_plural = 'CompilerDesignComments'


class ComputerOrganizationComments(Comments):
    post = models.ForeignKey(ComputerOrganization, on_delete=models.CASCADE,
                             related_name='ComputerOrganizationComments')

    class Meta:
        verbose_name_plural = 'ComputerOrganizationComments'


class DiscreteMathematicsComments(Comments):
    post = models.ForeignKey(DiscreteMathematics, on_delete=models.CASCADE, related_name='DiscreteMathematicsComments')

    class Meta:
        verbose_name_plural = 'DiscreteMathematicsComments'


class SoftwareEngineeringComments(Comments):
    post = models.ForeignKey(SoftwareEngineering, on_delete=models.CASCADE, related_name='SoftwareEngineeringComments')

    class Meta:
        verbose_name_plural = 'SoftwareEngineeringComments'


class CyberSecurityComments(Comments):
    post = models.ForeignKey(CyberSecurity, on_delete=models.CASCADE, related_name='CyberSecurityComments')

    class Meta:
        verbose_name_plural = 'CyberSecurityComments'


class DataMiningComments(Comments):
    post = models.ForeignKey(DataMining, on_delete=models.CASCADE, related_name='DataMiningComments')

    class Meta:
        verbose_name_plural = 'DataMiningComments'


class ArtificialIntelligenceComments(Comments):
    post = models.ForeignKey(ArtificialIntelligence, on_delete=models.CASCADE,
                             related_name='ArtificialIntelligenceComments')

    class Meta:
        verbose_name_plural = 'ArtificialIntelligenceComments'


class AutomataComments(Comments):
    post = models.ForeignKey(Automata, on_delete=models.CASCADE, related_name='AutomataComments')

    class Meta:
        verbose_name_plural = 'AutomataComments'


class ComputerGraphicsComments(Comments):
    post = models.ForeignKey(ComputerGraphics, on_delete=models.CASCADE, related_name='ComputerGraphicsComments')

    class Meta:
        verbose_name_plural = 'ComputerGraphicsComments'


class WebApiComments(Comments):
    post = models.ForeignKey(WebApi, on_delete=models.CASCADE, related_name='WebApiComments')

    class Meta:
        verbose_name_plural = 'WebApiComments'
