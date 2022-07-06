from django.db import models
from MainApp.models import LikeCommon, TutCommonParent
from django.urls import reverse_lazy
from tinymce.models import HTMLField


# Create your models here.
# Create your models here.

# Parent
class CExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CExercise Parent'

    def get_child(self):
        return CExercise.objects.all()


class CPlusExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CPlusExercise Parent'

    def get_child(self):
        return CPlusExercise.objects.all()


class PythonExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PythonExercise Parent'

    def get_child(self):
        return PythonExercise.objects.all()


class JavaExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaExercise Parent'

    def get_child(self):
        return JavaExercise.objects.all()


class KotlinExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'KotlinExercise Parent'

    def get_child(self):
        return KotlinExercise.objects.all()


class RExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'RExercise Parent'

    def get_child(self):
        return RExercise.objects.all()


class CSharpExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'CSharpExercise Parent'

    def get_child(self):
        return CSharpExercise.objects.all()


class SwiftExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SwiftExercise Parent'

    def get_child(self):
        return SwiftExercise.objects.all()


class JavaScriptExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'JavaScriptExercise Parent'

    def get_child(self):
        return JavaScriptExercise.objects.all()


class PHPExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PHPExercise Parent'

    def get_child(self):
        return PHPExercise.objects.all()


class DotNetExerciseParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'DotNetExercise Parent'

    def get_child(self):
        return DotNetExercise.objects.all()


class ExerciseCommon(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    viewcounter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class CExercise(ExerciseCommon):
    parent = models.ForeignKey(CExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:cexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = CQuestionAnswer.objects.all()
        return ls


class CPlusExercise(ExerciseCommon):
    parent = models.ForeignKey(CPlusExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CPlusExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:cplusexcisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = CplusQuestionAnswer.objects.all()
        return ls


class PythonExercise(ExerciseCommon):
    parent = models.ForeignKey(PythonExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PythonExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:pythonexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = PythonQuestionAnswer.objects.all()
        return ls


class JavaExercise(ExerciseCommon):
    parent = models.ForeignKey(JavaExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:javaexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = JavaQuestionAnswer.objects.all()
        return ls


class KotlinExercise(ExerciseCommon):
    parent = models.ForeignKey(KotlinExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'KotlinExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:kotlinexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = KotlinQuestionAnswer.objects.all()
        return ls


class RExercise(ExerciseCommon):
    parent = models.ForeignKey(RExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'RExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:rexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = RQuestionAnswer.objects.all()
        return ls


class CSharpExercise(ExerciseCommon):
    parent = models.ForeignKey(CSharpExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'CSharpExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:csharpexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = CSharpQuestionAnswer.objects.all()
        return ls


class SwiftExercise(ExerciseCommon):
    parent = models.ForeignKey(SwiftExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SwiftExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:swiftexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = SwiftQuestionAnswer.objects.all()
        return ls


class JavaScriptExercise(ExerciseCommon):
    parent = models.ForeignKey(JavaScriptExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'JavaScriptExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:javascriptexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = JavaScriptQuestionAnswer.objects.all()
        return ls


class PHPExercise(ExerciseCommon):
    parent = models.ForeignKey(PHPExerciseParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PHPExercise'

    def get_absolute_url(self):
        return f'{reverse_lazy("Exercise:phpexercisedetail", kwargs={"slug": self.slug})}'

    def questionlist(self):
        ls = PHPQuestionAnswer.objects.all()
        return ls


class DotNetExercise(ExerciseCommon):
    parent = models.ForeignKey(DotNetExerciseParent, on_delete=models.CASCADE, null=False)

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


# Like Button Model
class CExerciseLike(LikeCommon):
    post = models.ForeignKey(CExercise, on_delete=models.CASCADE)


class CPlusExerciseLike(LikeCommon):
    post = models.ForeignKey(CPlusExercise, on_delete=models.CASCADE)


class PythonExerciseLike(LikeCommon):
    post = models.ForeignKey(PythonExercise, on_delete=models.CASCADE)


class JavaExerciseLike(LikeCommon):
    post = models.ForeignKey(JavaExercise, on_delete=models.CASCADE)


class KotlinExerciseLike(LikeCommon):
    post = models.ForeignKey(KotlinExercise, on_delete=models.CASCADE)


class RExerciseLike(LikeCommon):
    post = models.ForeignKey(RExercise, on_delete=models.CASCADE)


class CSharpExerciseLike(LikeCommon):
    post = models.ForeignKey(CSharpExercise, on_delete=models.CASCADE)


class SwiftExerciseLike(LikeCommon):
    post = models.ForeignKey(SwiftExercise, on_delete=models.CASCADE)


class JavaScriptExerciseLike(LikeCommon):
    post = models.ForeignKey(JavaScriptExercise, on_delete=models.CASCADE)


class PHPExerciseLike(LikeCommon):
    post = models.ForeignKey(PHPExercise, on_delete=models.CASCADE)


class DotNetExerciseLike(LikeCommon):
    post = models.ForeignKey(DotNetExercise, on_delete=models.CASCADE)
