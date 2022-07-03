from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Therory Tut
class DBMS(TutCommon):
    class Meta:
        verbose_name_plural = 'DBMS'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:dbmsdetail", kwargs={"slug": self.slug})}'


class DataStructure(TutCommon):
    class Meta:
        verbose_name_plural = 'DataStructure'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:datastructuredetail", kwargs={"slug": self.slug})}'


class DAA(TutCommon):
    class Meta:
        verbose_name_plural = 'DAA'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:daadetail", kwargs={"slug": self.slug})}'


class OperatingSystem(TutCommon):
    class Meta:
        verbose_name_plural = 'OperatingSystem'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:operatingsystemdetail", kwargs={"slug": self.slug})}'


class ComputerNetwork(TutCommon):
    class Meta:
        verbose_name_plural = 'ComputerNetwork'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:computernetworkdetail", kwargs={"slug": self.slug})}'


class CompilerDesign(TutCommon):
    class Meta:
        verbose_name_plural = 'CompilerDesign'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:compilerdesigndetail", kwargs={"slug": self.slug})}'


class ComputerOrganization(TutCommon):
    class Meta:
        verbose_name_plural = 'ComputerOrganization'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:computerorganizationdetail", kwargs={"slug": self.slug})}'


class DiscreteMathematics(TutCommon):
    class Meta:
        verbose_name_plural = 'DiscreteMathematics'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:discretemathematicsdetail", kwargs={"slug": self.slug})}'


class SoftwareEngineering(TutCommon):
    class Meta:
        verbose_name_plural = 'SoftwareEngineering'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:softwareengineeringdetail", kwargs={"slug": self.slug})}'


class CyberSecurity(TutCommon):
    class Meta:
        verbose_name_plural = 'CyberSecurity'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:cybersecuritydetail", kwargs={"slug": self.slug})}'


class DataMining(TutCommon):
    class Meta:
        verbose_name_plural = 'DataMining'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:datamininganddatawarehousedetail", kwargs={"slug": self.slug})}'


class ArtificialIntelligence(TutCommon):
    class Meta:
        verbose_name_plural = 'ArtificialIntelligence'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:artificialintelligencedetail", kwargs={"slug": self.slug})}'


class Automata(TutCommon):
    class Meta:
        verbose_name_plural = 'Automata'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:automatadetail", kwargs={"slug": self.slug})}'


class ComputerGraphics(TutCommon):
    class Meta:
        verbose_name_plural = 'ComputerGraphics'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:computergraphicsdetail", kwargs={"slug": self.slug})}'


class WebApi(TutCommon):
    class Meta:
        verbose_name_plural = 'WebApi'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:webapidetail", kwargs={"slug": self.slug})}'


class DDBMS(TutCommon):
    class Meta:
        verbose_name_plural = 'DDBMS'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:ddbmsdetail", kwargs={"slug": self.slug})}'

