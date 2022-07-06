from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Programming'

urlpatterns = [
                  path('clanguage/', views.CView.as_view(), name='c'),
                  path('clanguage/<slug>/', views.CLanguageDetailView.as_view(), name='cdetail'),
                  path('cpluslanguage/', views.CPlusView.as_view(), name='cplus'),
                  path('cpluslanguage/<slug>/', views.CPlusLanguageDetailView.as_view(), name='cplusdetail'),
                  path('pythonlanguage/', views.PythonView.as_view(), name='python'),
                  path('pythonlanguage/<slug>/', views.PythonLanguageDetailView.as_view(), name='pythondetail'),
                  path('javalanguage/', views.JavaView.as_view(), name='java'),
                  path('javalanguage/<slug>/', views.JavaLanguageDetailView.as_view(), name='javadetail'),
                  path('androidlanguage/', views.AndroidView.as_view(), name='android'),
                  path('androidlanguage/<slug>/', views.AndroidLanguageDetailView.as_view(), name='androiddetail'),
                  path('kotlinlanguage/', views.KotlinView.as_view(), name='kotlin'),
                  path('kotlinlanguage/<slug>/', views.KotlinLanguageDetailView.as_view(), name='kotlindetail'),
                  path('rlanguage/', views.RView.as_view(), name='r'),
                  path('rlanguage/<slug>/', views.RLanguageDetailView.as_view(), name='rdetail'),
                  path('csharplanguage/', views.CSharpView.as_view(), name='csharp'),
                  path('csharplanguage/<slug>/', views.CSharpLanguageDetailView.as_view(), name='csharpdetail'),
                  path('swiftlanguage/', views.SwiftView.as_view(), name='swift'),
                  path('swiftlanguage/<slug>/', views.SwiftLanguageDetailView.as_view(), name='swiftdetail'),
                  path('javascriptlanguage/', views.JavaScriptView.as_view(), name='javascript'),
                  path('javascriptlanguage/<slug>/', views.JavaScriptLanguageDetailView.as_view(),
                       name='javascriptdetail'),
                  path('phplanguage/', views.PHPView.as_view(), name='php'),
                  path('phplanguage/<slug>/', views.PHPLanguageDetailView.as_view(), name='phpdetail'),
                  path('dotnetlanguage/', views.DotNetView.as_view(), name='dotnet'),
                  path('dotnetlanguage/<slug>/', views.DotNetLanguageDetailView.as_view(), name='dotnetdetail'),

              ]
