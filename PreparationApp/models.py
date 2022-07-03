from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Prepatation
class Aptitude(TutCommon):
    class Meta:
        verbose_name_plural = 'Aptitude'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:aptitudedetail", kwargs={"slug": self.slug})}'


class Reasoning(TutCommon):
    class Meta:
        verbose_name_plural = 'Reasoning'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:reasoningdetail", kwargs={"slug": self.slug})}'


class VerbalAbility(TutCommon):
    class Meta:
        verbose_name_plural = 'VerbalAbility'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:verbalabilitydetail", kwargs={"slug": self.slug})}'


class InterviewQuestion(TutCommon):
    class Meta:
        verbose_name_plural = 'InterviewQuestion'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:interviewquestiondetail", kwargs={"slug": self.slug})}'


class CompanyQuestion(TutCommon):
    class Meta:
        verbose_name_plural = 'CompanyQuestion'
       

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:companyquestiondetail", kwargs={"slug": self.slug})}'
