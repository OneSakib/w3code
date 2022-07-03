from django.db import models
from MainApp.models import Comments, HOST_NAME
from django.urls import reverse_lazy
from tinymce.models import HTMLField


# Create your models here.
# Create your models here.
class ExerciseCommon(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    viewcounter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class CExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'CExercise'
     

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:cexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = CQuestionAnswer.objects.all()
        return ls


class CPlusExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'CPlusExercise'
       
    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:cplusexcisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = CplusQuestionAnswer.objects.all()
        return ls


class PythonExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'PythonExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:pythonexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = PythonQuestionAnswer.objects.all()
        return ls


class JavaExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'JavaExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:javaexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = JavaQuestionAnswer.objects.all()
        return ls


class KotlinExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'KotlinExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:kotlinexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = KotlinQuestionAnswer.objects.all()
        return ls


class RExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'RExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:rexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = RQuestionAnswer.objects.all()
        return ls


class CSharpExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'CSharpExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:csharpexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = CSharpQuestionAnswer.objects.all()
        return ls


class SwiftExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'SwiftExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:swiftexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = SwiftQuestionAnswer.objects.all()
        return ls


class JavaScriptExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'JavaScriptExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:javascriptexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = JavaScriptQuestionAnswer.objects.all()
        return ls


class PHPExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'PHPExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:phpexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = PHPQuestionAnswer.objects.all()
        return ls


class DotNetExercise(ExerciseCommon):
    class Meta:
        verbose_name_plural = 'DotNetExercise'
      

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:dotnetexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = DotNetQuestionAnswer.objects.all()
        return ls


class QuestionAnswerCommon(models.Model):
    question = HTMLField()
    answer = HTMLField()

    class Meta:
        verbose_name_plural = 'Question and Answer'


class CQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(CExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class CplusQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(CPlusExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class CSharpQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(CSharpExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class DotNetQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(DotNetExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class JavaQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(JavaExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class KotlinQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(KotlinExercise, on_delete=models.CASCADE, related_name='question')


class PHPQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(PHPExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class PythonQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(PythonExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class JavaScriptQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(JavaScriptExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class RQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(RExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title


class SwiftQuestionAnswer(QuestionAnswerCommon):
    exercise = models.ForeignKey(SwiftExercise, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.exercise.title
