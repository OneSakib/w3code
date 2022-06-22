from django.db import models
from MainApp.models import TutCommon, Comments, HOST_NAME
from django.urls import reverse_lazy


# Create your models here.


# Prepatation
class Aptitude(TutCommon):
    class Meta:
        verbose_name_plural = 'Aptitude'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Preparation:aptitudedetail", kwargs={"slug": self.slug})}'


class Reasoning(TutCommon):
    class Meta:
        verbose_name_plural = 'Reasoning'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Preparation:reasoningdetail", kwargs={"slug": self.slug})}'


class VerbalAbility(TutCommon):
    class Meta:
        verbose_name_plural = 'VerbalAbility'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Preparation:verbalabilitydetail", kwargs={"slug": self.slug})}'


class InterviewQuestion(TutCommon):
    class Meta:
        verbose_name_plural = 'InterviewQuestion'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Preparation:interviewquestiondetail", kwargs={"slug": self.slug})}'


class CompanyQuestion(TutCommon):
    class Meta:
        verbose_name_plural = 'CompanyQuestion'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Preparation:companyquestiondetail", kwargs={"slug": self.slug})}'


# Comments
class AptitudeComments(Comments):
    post = models.ForeignKey(Aptitude, on_delete=models.CASCADE, related_name='AptitudeComments')

    class Meta:
        verbose_name_plural = 'AptitudeComments'


class ReasoningComments(Comments):
    post = models.ForeignKey(Reasoning, on_delete=models.CASCADE, related_name='ReasoningComments')

    class Meta:
        verbose_name_plural = 'ReasoningComments'


class VerbalAbilityComments(Comments):
    post = models.ForeignKey(VerbalAbility, on_delete=models.CASCADE, related_name='VerbalAbilityComments')

    class Meta:
        verbose_name_plural = 'VerbalAbilityComments'


class InterviewQuestionComments(Comments):
    post = models.ForeignKey(InterviewQuestion, on_delete=models.CASCADE, related_name='InterviewQuestionComments')

    class Meta:
        verbose_name_plural = 'InterviewQuestionComments'


class CompanyQuestionComments(Comments):
    post = models.ForeignKey(CompanyQuestion, on_delete=models.CASCADE, related_name='CompanyQuestionComments')

    class Meta:
        verbose_name_plural = 'CompanyQuestionComments'
