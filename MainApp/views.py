from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, FormView, DetailView, View
from .models import *
from .forms import *
from next_prev import next_in_order, prev_in_order
from ProgrammingApp import models as prog
from ProgrammingApp.models import *
from PreparationApp.models import *
from TheoryApp.models import *
from PythonApp.models import *
from JavaApp.models import *
from JavaScriptApp.models import *
from DatabaseApp.models import *
from WebApp.models import *
from MsApp.models import *
from VCApp.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'host_name': settings.HOST_NAME
        }
        return render(request, 'w3c/index.html', context)


def OnlineCompiler(request, slug):
    code = None
    slug = str(slug).strip()
    if slug.lower() == 'python':
        code = 'https://trinket.io/embed/python3/70715ff3af'
    elif slug.lower() == 'java':
        code = 'https://trinket.io/embed/java/ebdae30f29'
    elif slug.lower() == 'r':
        code = 'https://trinket.io/embed/R/b0a483cf9b'
    elif slug.lower() == 'html':
        code = 'https://trinket.io/embed/html/592c0c15e7'
    context = {
        'code': code
    }
    return render(request, 'w3c/onlineide.html', context)


class BlogView(ListView):
    template_name = 'w3c/blog.html'
    model = Blogs


class BlogDetailView(DetailView, FormView):
    template_name = 'w3c/blogdetail.html'
    form_class = BlogCommentForm
    model = Blogs

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = BlogComments.objects.filter(post=self.object)
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('w3c:blogdetail', kwargs={'slug': self.kwargs['slug']}))


@method_decorator(login_required(login_url='/'), name='dispatch')
class CommentsView(View):
    def get(self, request):
        return render(request, 'comments/list.html')


@method_decorator(login_required(login_url='/'), name='dispatch')
class CommentsDetailView(View):
    def get(self, request, slug):
        name = str(slug).strip()
        obj = None
        title = 'Comments'
        if name == 'c':
            obj = CLanguageComments.objects.all()
            title = 'C Language Comments'
        elif name == 'cplus':
            obj = CplusLanguageComments.objects.all()
            title = 'C++ Language Comments'
        elif name == 'java':
            obj = JavaLanguageComments.objects.all()
            title = 'Java Language Comments'
        elif name == 'python':
            obj = PythonLanguageComments.objects.all()
            title = 'Python Language Comments'
        elif name == 'android':
            obj = CLanguageComments.objects.all()
            title = 'Android Comments'
        elif name == 'kotlin':
            obj = KotlinLanguageComments.objects.all()
            title = 'Kotlin Language Comments'
        elif name == 'r':
            obj = RLanguageComments.objects.all()
            title = 'R Language Comments'
        elif name == 'csharp':
            obj = CsharpLanguageComments.objects.all()
            title = 'C# Language Comments'
        elif name == 'swift':
            obj = SwiftLanguageComments.objects.all()
            title = 'Swift Language Comments'
        elif name == 'js':
            obj = JavaScriptLanguageComments.objects.all()
            title = 'JavaScript Language Comments'
        elif name == 'php':
            obj = PHPLanguageComments.objects.all()
            title = 'PHP Language Comments'
        elif name == 'dotnet':
            obj = DotNetLanguageComments.objects.all()
            title = '.Net Language Comments'
        elif name == 'aptitude':
            obj = AptitudeComments.objects.all()
            title = 'Aptitude Comments'
        elif name == 'reasoning':
            obj = ReasoningComments.objects.all()
            title = 'Reasoning Comments'
        elif name == 'verbal':
            obj = VerbalAbilityComments.objects.all()
            title = 'VerbalAbility Comments'
        elif name == 'interview':
            obj = InterviewQuestionComments.objects.all()
            title = 'Interview Question Comments'
        elif name == 'company':
            obj = CompanyQuestionComments.objects.all()
            title = 'Company Question Comments'
        elif name == 'dbms':
            obj = DBMSComments.objects.all()
            title = 'DBMS Comments'
        elif name == 'daa':
            obj = DAAComments.objects.all()
            title = 'DAA Comments'
        elif name == 'ds':
            obj = DataStructureComments.objects.all()
            title = 'Data Structure Comments'
        elif name == 'os':
            obj = OperatingSystemComments.objects.all()
            title = 'Operating System Comments'
        elif name == 'cn':
            obj = ComputerNetworkComments.objects.all()
            title = 'Computer Network Comments'
        elif name == 'cd':
            obj = CompilerDesignComments.objects.all()
            title = 'Compiler Design Comments'
        elif name == 'co':
            obj = ComputerOrganizationComments.objects.all()
            title = 'Computer Organization Comments'
        elif name == 'dsm':
            obj = DiscreteMathematicsComments.objects.all()
            title = 'Discrete Mathematics Comments'
        elif name == 'se':
            obj = SoftwareEngineeringComments.objects.all()
            title = 'Software Engineering Comments'
        elif name == 'cs':
            obj = CyberSecurityComments.objects.all()
            title = 'Cyber Security Comments'
        elif name == 'dm':
            obj = DataMiningComments.objects.all()
            title = 'Data Mining Comments'
        elif name == 'ai':
            obj = ArtificialIntelligenceComments.objects.all()
            title = 'Artificial Intelligence Comments'
        elif name == 'at':
            obj = AutomataComments.objects.all()
            title = 'Automata Comments'
        elif name == 'cg':
            obj = ComputerGraphicsComments.objects.all()
            title = 'Computer Graphics Comments'
        elif name == 'wa':
            obj = WebApiComments.objects.all()
            title = 'Web API Comments'
        elif name == 'flask':
            obj = FlaskComments.objects.all()
            title = 'Flask Comments'
        elif name == 'ml':
            obj = MachineLearningComments.objects.all()
            title = 'Machine Learning Comments'
        elif name == 'numpy':
            obj = NumpysComments.objects.all()
            title = 'Numpys Comments'
        elif name == 'tkinter':
            obj = TkintersComments.objects.all()
            title = 'Tkinters Comments'
        elif name == 'pytorch':
            obj = PytorchsComments.objects.all()
            title = 'Pytorch Comments'
        elif name == 'pygame':
            obj = PygamesComments.objects.all()
            title = 'Pygame Comments'
        elif name == 'scipy':
            obj = ScipysComments.objects.all()
            title = 'Scipy Comments'
        elif name == 'pandas':
            obj = PandassComments.objects.all()
            title = 'Pandas Comments'
        elif name == 'opencv':
            obj = OpenCVsComments.objects.all()
            title = 'OpenCV Comments'
        elif name == 'matplotlib':
            obj = MatplotlibsComments.objects.all()
            title = 'Matplotlib Comments'
        elif name == 'selenium':
            obj = SeleniumsComments.objects.all()
            title = 'Selenium Comments'
        elif name == 'kivy':
            obj = KivysComments.objects.all()
            title = 'Kivys Comments'
        elif name == 'jupyter':
            obj = JupytersComments.objects.all()
            title = 'Jupyter Comments'
        elif name == 'dsc':
            obj = DataScienceComments.objects.all()
            title = 'Data Science Comments'
        elif name == 'dl':
            obj = DeepLearningComments.objects.all()
            title = 'Deep Learning Comments'
        elif name == 'pillow':
            obj = PillowsComments.objects.all()
            title = 'Pillows Comments'
        elif name == 'tensorflow':
            obj = TensorflowsComments.objects.all()
            title = 'Tensorflow Comments'
        elif name == 'django':
            obj = DjangoComments.objects.all()
            title = 'Django Comments'
        elif name == 'servlet':
            obj = ServletsComments.objects.all()
            title = 'Servlet Comments'
        elif name == 'jsp':
            obj = JSPsComments.objects.all()
            title = 'JSP Comments'
        elif name == 'sb':
            obj = SpringBootComments.objects.all()
            title = 'SpringBoot Comments'
        elif name == 'sf':
            obj = SpringFrameworkComments.objects.all()
            title = 'Spring Framework Comments'
        elif name == 'hibernate':
            obj = HibernatesComments.objects.all()
            title = 'Hibernate Comments'
        elif name == 'jsw':
            obj = JavaSwingsComments.objects.all()
            title = 'Java Swing Comments'
        elif name == 'jfx':
            obj = JavaFXsComments.objects.all()
            title = 'JavaFX Comments'
        elif name == 'jawt':
            obj = JavaAWTComments.objects.all()
            title = 'Java AWT Comments'
        elif name == 'jcol':
            obj = CollectionsComments.objects.all()
            title = 'JAVA Collection Comments'
        elif name == 'jdate':
            obj = JavaDateComments.objects.all()
            title = 'Java Date Comments'
        elif name == 'jio':
            obj = JavaIOComments.objects.all()
            title = 'Java I/O Comments'
        elif name == 'jquery':
            obj = JqueryComments.objects.all()
            title = 'Jquery Comments'
        elif name == 'angular':
            obj = AngularjsComments.objects.all()
            title = 'Angularjs Comments'
        elif name == 'node':
            obj = NodejsComments.objects.all()
            title = 'Nodejs Comments'
        elif name == 'express':
            obj = ExpressjsComments.objects.all()
            title = 'Expressjs Comments'
        elif name == 'react':
            obj = ReactjsComments.objects.all()
            title = 'Reactjs Comments'
        elif name == 'tsc':
            obj = TypeScriptsComments.objects.all()
            title = 'TypeScript Comments'
        elif name == 'vue':
            obj = VUEjsComments.objects.all()
            title = 'VUEjs Comments'
        elif name == 'mysql':
            obj = MysqlDBComments.objects.all()
            title = 'MysqlDB Comments'
        elif name == 'mongo':
            obj = MongoDBComments.objects.all()
            title = 'MongoDB Comments'
        elif name == 'postgre':
            obj = PostgreSQLDBComments.objects.all()
            title = 'PostgreSQLDB Comments'
        elif name == 'oracle':
            obj = OracleDBComments.objects.all()
            title = 'OracleDB Comments'
        elif name == 'sqlite':
            obj = SqliteDBComments.objects.all()
            title = 'SqliteDB Comments'
        elif name == 'maria':
            obj = MariaDBComments.objects.all()
            title = 'MariaDB Comments'
        elif name == 'html':
            obj = HTMLsComments.objects.all()
            title = 'HTML Comments'
        elif name == 'css':
            obj = CSSsComments.objects.all()
            title = 'CSS Comments'
        elif name == 'laravel':
            obj = LaravelsComments.objects.all()
            title = 'Laravel Comments'
        elif name == 'wordpress':
            obj = WordpressComments.objects.all()
            title = 'Wordpress Comments'
        elif name == 'json':
            obj = JSONsComments.objects.all()
            title = 'JSON Comments'
        elif name == 'ajax':
            obj = AjaxsComments.objects.all()
            title = 'Ajax Comments'
        elif name == 'bootstrap':
            obj = BootstrapsComments.objects.all()
            title = 'Bootstrap Comments'
        elif name == 'word':
            obj = MSWordComments.objects.all()
            title = 'MSWord Comments'
        elif name == 'excel':
            obj = MSExcelComments.objects.all()
            title = 'MSExcel Comments'
        elif name == 'pp':
            obj = MSPowerpointComments.objects.all()
            title = 'MSPowerpoint Comments'
        elif name == 'on':
            obj = MSOneNoteComments.objects.all()
            title = 'MSOneNot eComments'
        elif name == 'docker':
            obj = DockerComments.objects.all()
            title = 'Docker Comments'
        elif name == 'git':
            obj = GitsComments.objects.all()
            title = 'Gits Comments'
        elif name == 'github':
            obj = GithubsComments.objects.all()
            title = 'Github Comments'
        if obj != None:
            obj = obj[:50:-1]

        context = {
            'obj': obj,
            'title': title
        }
        return render(request, 'comments/detail.html', context)

    def post(self, request, slug):
        pk = request.POST.get('id')
        name = str(slug).strip()
        if name == 'c':
            obj = CLanguageComments
        elif name == 'cplus':
            obj = CplusLanguageComments
        elif name == 'java':
            obj = JavaLanguageComments
        elif name == 'python':
            obj = PythonLanguageComments
        elif name == 'android':
            obj = CLanguageComments
        elif name == 'kotlin':
            obj = KotlinLanguageComments
        elif name == 'r':
            obj = RLanguageComments
        elif name == 'csharp':
            obj = CsharpLanguageComments
        elif name == 'swift':
            obj = SwiftLanguageComments
        elif name == 'js':
            obj = JavaScriptLanguageComments
        elif name == 'php':
            obj = PHPLanguageComments
        elif name == 'dotnet':
            obj = DotNetLanguageComments
        elif name == 'aptitude':
            obj = AptitudeComments
        elif name == 'reasoning':
            obj = ReasoningComments
        elif name == 'verbal':
            obj = VerbalAbilityComments
        elif name == 'interview':
            obj = InterviewQuestionComments
        elif name == 'company':
            obj = CompanyQuestionComments
        elif name == 'dbms':
            obj = DBMSComments
        elif name == 'daa':
            obj = DAAComments
        elif name == 'ds':
            obj = DataStructureComments
        elif name == 'os':
            obj = OperatingSystemComments
        elif name == 'cn':
            obj = ComputerNetworkComments
        elif name == 'cd':
            obj = CompilerDesignComments
        elif name == 'co':
            obj = ComputerOrganizationComments
        elif name == 'dsm':
            obj = DiscreteMathematicsComments
        elif name == 'se':
            obj = SoftwareEngineeringComments
        elif name == 'cs':
            obj = CyberSecurityComments
        elif name == 'dm':
            obj = DataMiningComments
        elif name == 'ai':
            obj = ArtificialIntelligenceComments
        elif name == 'at':
            obj = AutomataComments
        elif name == 'cg':
            obj = ComputerGraphicsComments
        elif name == 'wa':
            obj = WebApiComments
        elif name == 'flask':
            obj = FlaskComments
        elif name == 'ml':
            obj = MachineLearningComments
        elif name == 'numpy':
            obj = NumpysComments
        elif name == 'tkinter':
            obj = TkintersComments
        elif name == 'pytorch':
            obj = PytorchsComments
        elif name == 'pygame':
            obj = PygamesComments
        elif name == 'scipy':
            obj = ScipysComments
        elif name == 'pandas':
            obj = PandassComments
        elif name == 'opencv':
            obj = OpenCVsComments
        elif name == 'matplotlib':
            obj = MatplotlibsComments
        elif name == 'selenium':
            obj = SeleniumsComments
        elif name == 'kivy':
            obj = KivysComments
        elif name == 'jupyter':
            obj = JupytersComments
        elif name == 'dsc':
            obj = DataScienceComments
        elif name == 'dl':
            obj = DeepLearningComments
        elif name == 'pillow':
            obj = PillowsComments
        elif name == 'tensorflow':
            obj = TensorflowsComments
        elif name == 'django':
            obj = DjangoComments
        elif name == 'servlet':
            obj = ServletsComments
        elif name == 'jsp':
            obj = JSPsComments
        elif name == 'sb':
            obj = SpringBootComments
        elif name == 'sf':
            obj = SpringFrameworkComments
        elif name == 'hibernate':
            obj = HibernatesComments
        elif name == 'jsw':
            obj = JavaSwingsComments
        elif name == 'jfx':
            obj = JavaFXsComments
        elif name == 'jawt':
            obj = JavaAWTComments
        elif name == 'jcol':
            obj = CollectionsComments
        elif name == 'jdate':
            obj = JavaDateComments
        elif name == 'jio':
            obj = JavaIOComments
        elif name == 'jquery':
            obj = JqueryComments
        elif name == 'angular':
            obj = AngularjsComments
        elif name == 'node':
            obj = NodejsComments
        elif name == 'express':
            obj = ExpressjsComments
        elif name == 'react':
            obj = ReactjsComments
        elif name == 'tsc':
            obj = TypeScriptsComments
        elif name == 'vue':
            obj = VUEjsComments
        elif name == 'mysql':
            obj = MysqlDBComments
        elif name == 'mongo':
            obj = MongoDBComments
        elif name == 'postgre':
            obj = PostgreSQLDBComments
        elif name == 'oracle':
            obj = OracleDBComments
        elif name == 'sqlite':
            obj = SqliteDBComments
        elif name == 'maria':
            obj = MariaDBComments
        elif name == 'html':
            obj = HTMLsComments
        elif name == 'css':
            obj = CSSsComments
        elif name == 'laravel':
            obj = LaravelsComments
        elif name == 'wordpress':
            obj = WordpressComments
        elif name == 'json':
            obj = JSONsComments
        elif name == 'ajax':
            obj = AjaxsComments
        elif name == 'bootstrap':
            obj = BootstrapsComments
        elif name == 'word':
            obj = MSWordComments
        elif name == 'excel':
            obj = MSExcelComments
        elif name == 'pp':
            obj = MSPowerpointComments
        elif name == 'on':
            obj = MSOneNoteComments
        elif name == 'docker':
            obj = DockerComments
        elif name == 'git':
            obj = GitsComments
        elif name == 'github':
            obj = GithubsComments
        if obj != None:
            obj = obj.objects.get(pk=pk)
            obj.delete()
        return HttpResponseRedirect(reverse_lazy('w3c:commentsdetail', kwargs={'slug': slug}))
