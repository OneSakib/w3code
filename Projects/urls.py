from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Projects'

urlpatterns = [
                  path('cprojects/', views.CProjectsView.as_view(), name='cprojects'),
                  path('cprojects/<slug>/', views.CProjectsDetailView.as_view(), name='cprojectsdetail'),
                  path('cplusprojects/', views.CPlusProjectsView.as_view(), name='cplusprojects'),
                  path('cplusprojects/<slug>/', views.CPlusProjectsDetailView.as_view(), name='cplusprojectsdetail'),
                  path('pythonprojects/', views.PythonProjectsView.as_view(), name='pythonprojects'),
                  path('pythonprojects/<slug>/', views.PythonProjectsDetailView.as_view(),
                       name='pythonprojectsdetail'),
                  path('javaprojects/', views.JavaProjectsView.as_view(), name='javaprojects'),
                  path('javaprojects/<slug>/', views.JavaProjectsDetailView.as_view(), name='javaprojectsdetail'),
                  path('kotlinprojects/', views.KotlinProjectsView.as_view(), name='kotlinprojects'),
                  path('kotlin[rojects/<slug>/', views.KotlinProjectsDetailView.as_view(),
                       name='kotlinprojectsdetail'),
                  path('rprojects/', views.RProjectsView.as_view(), name='rprojects'),
                  path('rprojects/<slug>/', views.RProjectsDetailView.as_view(), name='rprojectsdetail'),
                  path('csharpprojects/', views.CSharpProjectsView.as_view(), name='csharpprojects'),
                  path('csharpprojects/<slug>/', views.CSharpProjectsDetailView.as_view(),
                       name='csharpprojectsdetail'),
                  path('swiftprojects/', views.SwiftProjectsView.as_view(), name='swiftprojects'),
                  path('swiftprojects/<slug>/', views.SwiftProjectsDetailView.as_view(), name='swiftprojectsdetail'),
                  path('javascriptprojects/', views.JavaScriptProjectsView.as_view(), name='javascriptprojects'),
                  path('javascriptprojects/<slug>/', views.JavaScriptProjectsDetailView.as_view(),
                       name='javascriptprojectsdetail'),
                  path('phpprojects/', views.PHPProjectsView.as_view(), name='phpprojects'),
                  path('phpprojects/<slug>/', views.PHPProjectsDetailView.as_view(), name='phpprojectsdetail'),
                  path('androidprojects/', views.AndroidProjectView.as_view(), name='androidprojects'),
                  path('androidprojects/<slug>/', views.AndroidProjectDetailView.as_view(),
                       name='androidprojectsdetail'),
                  path('dotnetprojects/', views.DotNetProjectsView.as_view(), name='dotnetprojects'),
                  path('dotnetprojects/<slug>/', views.DotNetProjectsDetailView.as_view(),
                       name='dotnetprojectsdetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
