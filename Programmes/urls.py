from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Programme'

urlpatterns = [
                  path('cprogramme/', views.CProgrammeView.as_view(), name='cprogramme'),
                  path('cprogramme/<slug>/', views.CProgrammeDetailView.as_view(), name='cprogrammedetail'),
                  path('cplusprogramme/', views.CPlusProgrammeView.as_view(), name='cplusprogramme'),
                  path('cplusprogramme/<slug>/', views.CPlusProgrammeDetailView.as_view(), name='cplusprogrammedetail'),
                  path('pythonprogramme/', views.PythonProgrammeView.as_view(), name='pythonprogramme'),
                  path('pythonprogramme/<slug>/', views.PythonProgrammeDetailView.as_view(),
                       name='pythonprogrammedetail'),
                  path('javaprogramme/', views.JavaProgrammeView.as_view(), name='javaprogramme'),
                  path('javaprogramme/<slug>/', views.JavaProgrammeDetailView.as_view(), name='javaprogrammedetail'),
                  path('kotlinprogramme/', views.KotlinProgrammeView.as_view(), name='kotlinprogramme'),
                  path('kotlinprogramme/<slug>/', views.KotlinProgrammeDetailView.as_view(),
                       name='kotlinprogrammedetail'),
                  path('rprogramme/', views.RProgrammeView.as_view(), name='rprogramme'),
                  path('rprogramme/<slug>/', views.RProgrammeDetailView.as_view(), name='rprogrammedetail'),
                  path('csharpprogramme/', views.CSharpProgrammeView.as_view(), name='csharpprogramme'),
                  path('csharpprogramme/<slug>/', views.CSharpProgrammeDetailView.as_view(),
                       name='csharpprogrammedetail'),
                  path('swiftprogramme/', views.SwiftProgrammeView.as_view(), name='swiftprogramme'),
                  path('swiftprogramme/<slug>/', views.SwiftProgrammeDetailView.as_view(), name='swiftprogrammedetail'),
                  path('javascriptprogramme/', views.JavaScriptProgrammeView.as_view(), name='javascriptprogramme'),
                  path('javascriptprogramme/<slug>/', views.JavaScriptProgrammeDetailView.as_view(),
                       name='javascriptprogrammedetail'),
                  path('phpprogramme/', views.PHPProgrammeView.as_view(), name='phpprogramme'),
                  path('phpprogramme/<slug>/', views.PHPProgrammeDetailView.as_view(), name='phpprogrammedetail'),
                  path('dotnetprogramme/', views.DotNetProgrammeView.as_view(), name='dotnetprogramme'),
                  path('dotnetprogramme/<slug>/', views.DotNetProgrammeDetailView.as_view(),
                       name='dotnetprogrammedetail'),
              ]
