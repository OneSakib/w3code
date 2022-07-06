from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Exercise'

urlpatterns = [
                  path('cexercise/', views.CExerciseView.as_view(), name='cexercise'),
                  path('cexercise/<slug>/', views.CExerciseDetailView.as_view(), name='cexercisedetail'),
                  path('cplusexcise/', views.CPlusExerciseView.as_view(), name='cplusexcise'),
                  path('cplusexcise/<slug>/', views.CPlusExerciseDetailView.as_view(), name='cplusexcisedetail'),
                  path('pythonexercise/', views.PythonExerciseView.as_view(), name='pythonexercise'),
                  path('pythonexercise/<slug>/', views.PythonExerciseDetailView.as_view(), name='pythonexercisedetail'),
                  path('javaexercise/', views.JavaExerciseView.as_view(), name='javaexercise'),
                  path('javaexercise/<slug>/', views.JavaExerciseDetailView.as_view(), name='javaexercisedetail'),
                  path('kotlinexercise/', views.KotlinExerciseView.as_view(), name='kotlinexercise'),
                  path('kotlinexercise/<slug>/', views.KotlinExerciseDetailView.as_view(), name='kotlinexercisedetail'),
                  path('rexercise/', views.RExerciseView.as_view(), name='rexercise'),
                  path('rexercise/<slug>/', views.RExerciseDetailView.as_view(), name='rexercisedetail'),
                  path('csharpexercise/', views.CSharpExerciseView.as_view(), name='csharpexercise'),
                  path('csharpexercise/<slug>/', views.CSharpExerciseDetailView.as_view(), name='csharpexercisedetail'),
                  path('swiftexercise/', views.SwiftExerciseView.as_view(), name='swiftexercise'),
                  path('swiftexercise/<slug>/', views.SwiftExerciseDetailView.as_view(), name='swiftexercisedetail'),
                  path('javascriptexercise/', views.JavaScriptExerciseView.as_view(), name='javascriptexercise'),
                  path('javascriptexercise/<slug>/', views.JavaScriptExerciseDetailView.as_view(),
                       name='javascriptexercisedetail'),
                  path('phpexercise/', views.PHPExerciseView.as_view(), name='phpexercise'),
                  path('phpexercise/<slug>/', views.PHPExerciseDetailView.as_view(), name='phpexercisedetail'),
                  path('dotnetexercise/', views.DotNetExerciseView.as_view(), name='dotnetexercise'),
                  path('dotnetexercise/<slug>/', views.DotNetExerciseDetailView.as_view(), name='dotnetexercisedetail'),
              ]
