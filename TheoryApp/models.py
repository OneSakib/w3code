from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.
# Parent
class DBMSParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DBMS Parent'

    def get_child(self):
        return DBMS.objects.all()


class DataStructureParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DataStructure Parent'

    def get_child(self):
        return DataStructure.objects.all()


class DAAParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DAA Parent'

    def get_child(self):
        return DAA.objects.all()


class OperatingSystemParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'OperatingSystem Parent'

    def get_child(self):
        return OperatingSystem.objects.all()


class ComputerNetworkParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'ComputerNetwork Parent'

    def get_child(self):
        return ComputerNetwork.objects.all()


class CompilerDesignParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CompilerDesign Parent'

    def get_child(self):
        return CompilerDesign.objects.all()


class ComputerOrganizationParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'ComputerOrganization Parent'

    def get_child(self):
        return ComputerOrganization.objects.all()


class DiscreteMathematicsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DiscreteMathematics Parent'

    def get_child(self):
        return DiscreteMathematics.objects.all()


class SoftwareEngineeringParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SoftwareEngineering Parent'

    def get_child(self):
        return SoftwareEngineering.objects.all()


class CyberSecurityParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CyberSecurity Parent'

    def get_child(self):
        return CyberSecurity.objects.all()


class DataMiningParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DataMining Parent'

    def get_child(self):
        return DataMining.objects.all()


class ArtificialIntelligenceParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'ArtificialIntelligence Parent'

    def get_child(self):
        return ArtificialIntelligence.objects.all()


class AutomataParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Automata Parent'

    def get_child(self):
        return Automata.objects.all()


class ComputerGraphicsParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'ComputerGraphics Parent'

    def get_child(self):
        return ComputerGraphics.objects.all()


class WebApiParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'WebApi Parent'

    def get_child(self):
        return WebApi.objects.all()


class DDBMSParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DDBMS Parent'

    def get_child(self):
        return DDBMS.objects.all()


# Child
class DBMS(TutCommon):
    parent = models.ForeignKey(DBMSParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DBMS'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:dbmsdetail", kwargs={"slug": self.slug})}'


class DataStructure(TutCommon):
    parent = models.ForeignKey(DataStructureParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DataStructure'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:datastructuredetail", kwargs={"slug": self.slug})}'


class DAA(TutCommon):
    parent = models.ForeignKey(DAAParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DAA'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:daadetail", kwargs={"slug": self.slug})}'


class OperatingSystem(TutCommon):
    parent = models.ForeignKey(OperatingSystemParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'OperatingSystem'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:operatingsystemdetail", kwargs={"slug": self.slug})}'


class ComputerNetwork(TutCommon):
    parent = models.ForeignKey(ComputerNetworkParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'ComputerNetwork'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:computernetworkdetail", kwargs={"slug": self.slug})}'


class CompilerDesign(TutCommon):
    parent = models.ForeignKey(CompilerDesignParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CompilerDesign'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:compilerdesigndetail", kwargs={"slug": self.slug})}'


class ComputerOrganization(TutCommon):
    parent = models.ForeignKey(ComputerOrganizationParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'ComputerOrganization'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:computerorganizationdetail", kwargs={"slug": self.slug})}'


class DiscreteMathematics(TutCommon):
    parent = models.ForeignKey(DiscreteMathematicsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DiscreteMathematics'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:discretemathematicsdetail", kwargs={"slug": self.slug})}'


class SoftwareEngineering(TutCommon):
    parent = models.ForeignKey(SoftwareEngineeringParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SoftwareEngineering'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:softwareengineeringdetail", kwargs={"slug": self.slug})}'


class CyberSecurity(TutCommon):
    parent = models.ForeignKey(CyberSecurityParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CyberSecurity'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:cybersecuritydetail", kwargs={"slug": self.slug})}'


class DataMining(TutCommon):
    parent = models.ForeignKey(DataMiningParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DataMining'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:datamininganddatawarehousedetail", kwargs={"slug": self.slug})}'


class ArtificialIntelligence(TutCommon):
    parent = models.ForeignKey(ArtificialIntelligenceParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'ArtificialIntelligence'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:artificialintelligencedetail", kwargs={"slug": self.slug})}'


class Automata(TutCommon):
    parent = models.ForeignKey(AutomataParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Automata'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:automatadetail", kwargs={"slug": self.slug})}'


class ComputerGraphics(TutCommon):
    parent = models.ForeignKey(ComputerGraphicsParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'ComputerGraphics'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:computergraphicsdetail", kwargs={"slug": self.slug})}'


class WebApi(TutCommon):
    parent = models.ForeignKey(WebApiParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'WebApi'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:webapidetail", kwargs={"slug": self.slug})}'


class DDBMS(TutCommon):
    parent = models.ForeignKey(DDBMSParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'DDBMS'

    def get_absolute_url(self):
        return f'{reverse_lazy("Theory:ddbmsdetail", kwargs={"slug": self.slug})}'


# Like Counter
class DBMSLike(LikeCommon):
    post = models.ForeignKey(DBMS, on_delete=models.CASCADE)


class DataStructureLike(LikeCommon):
    post = models.ForeignKey(DataStructure, on_delete=models.CASCADE)


class DAALike(LikeCommon):
    post = models.ForeignKey(DAA, on_delete=models.CASCADE)


class OperatingSystemLike(LikeCommon):
    post = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)


class ComputerNetworkLike(LikeCommon):
    post = models.ForeignKey(ComputerNetwork, on_delete=models.CASCADE)


class CompilerDesignLike(LikeCommon):
    post = models.ForeignKey(CompilerDesign, on_delete=models.CASCADE)


class ComputerOrganizationLike(LikeCommon):
    post = models.ForeignKey(ComputerOrganization, on_delete=models.CASCADE)


class DiscreteMathematicsLike(LikeCommon):
    post = models.ForeignKey(DiscreteMathematics, on_delete=models.CASCADE)


class SoftwareEngineeringLike(LikeCommon):
    post = models.ForeignKey(SoftwareEngineering, on_delete=models.CASCADE)


class CyberSecurityLike(LikeCommon):
    post = models.ForeignKey(CyberSecurity, on_delete=models.CASCADE)


class DataMiningLike(LikeCommon):
    post = models.ForeignKey(DataMining, on_delete=models.CASCADE)


class ArtificialIntelligenceLike(LikeCommon):
    post = models.ForeignKey(ArtificialIntelligence, on_delete=models.CASCADE)


class AutomataLike(LikeCommon):
    post = models.ForeignKey(Automata, on_delete=models.CASCADE)


class ComputerGraphicsLike(LikeCommon):
    post = models.ForeignKey(ComputerGraphics, on_delete=models.CASCADE)


class WebApiLike(LikeCommon):
    post = models.ForeignKey(WebApi, on_delete=models.CASCADE)


class DDBMSLike(LikeCommon):
    post = models.ForeignKey(DDBMS, on_delete=models.CASCADE)
