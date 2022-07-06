from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.
# Parent
# Parent
class AptitudeParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Aptitude Parent'

    def get_child(self):
        return Aptitude.objects.all()


class ReasoningParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'Reasoning Parent'

    def get_child(self):
        return Reasoning.objects.all()


class VerbalAbilityParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'VerbalAbility Parent'

    def get_child(self):
        return VerbalAbility.objects.all()


class InterviewQuestionParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'InterviewQuestion Parent'

    def get_child(self):
        return InterviewQuestion.objects.all()


class CompanyQuestionParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CompanyQuestion Parent'

    def get_child(self):
        return CompanyQuestion.objects.all()


# Child
# Prepatation
class Aptitude(TutCommon):
    parent = models.ForeignKey(AptitudeParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Aptitude'

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:aptitudedetail", kwargs={"slug": self.slug})}'


class Reasoning(TutCommon):
    parent = models.ForeignKey(ReasoningParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Reasoning'

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:reasoningdetail", kwargs={"slug": self.slug})}'


class VerbalAbility(TutCommon):
    parent = models.ForeignKey(VerbalAbilityParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'VerbalAbility'

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:verbalabilitydetail", kwargs={"slug": self.slug})}'


class InterviewQuestion(TutCommon):
    parent = models.ForeignKey(InterviewQuestionParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'InterviewQuestion'

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:interviewquestiondetail", kwargs={"slug": self.slug})}'


class CompanyQuestion(TutCommon):
    parent = models.ForeignKey(CompanyQuestionParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CompanyQuestion'

    def get_absolute_url(self):
        return f'{reverse_lazy("Preparation:companyquestiondetail", kwargs={"slug": self.slug})}'


# Like Counter
class AptitudeLike(LikeCommon):
    post = models.ForeignKey(Aptitude, on_delete=models.CASCADE)


class ReasoningLike(LikeCommon):
    post = models.ForeignKey(Reasoning, on_delete=models.CASCADE)


class VerbalAbilityLike(LikeCommon):
    post = models.ForeignKey(VerbalAbility, on_delete=models.CASCADE)


class InterviewQuestionLike(LikeCommon):
    post = models.ForeignKey(InterviewQuestion, on_delete=models.CASCADE)


class CompanyQuestionLike(LikeCommon):
    post = models.ForeignKey(CompanyQuestion, on_delete=models.CASCADE)
