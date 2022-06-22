from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Programming'

urlpatterns = [
                  path('c/', views.CView.as_view(), name='c'),
                  path('c/<slug>/', views.CView.as_view(), name='cdetail'),
                  path('cplus/', views.CPlusView.as_view(), name='cplus'),
                  path('cplus/<slug>/', views.CPlusView.as_view(), name='cplusdetail'),
                  path('python/', views.PythonView.as_view(), name='python'),
                  path('python/<slug>/', views.PythonView.as_view(), name='pythondetail'),
                  path('java/', views.JavaView.as_view(), name='java'),
                  path('java/<slug>/', views.JavaView.as_view(), name='javadetail'),
                  path('android/', views.AndroidView.as_view(), name='android'),
                  path('android/<slug>/', views.AndroidView.as_view(), name='androiddetail'),
                  path('kotlin/', views.KotlinView.as_view(), name='kotlin'),
                  path('kotlin/<slug>/', views.KotlinView.as_view(), name='kotlindetail'),
                  path('r/', views.RView.as_view(), name='r'),
                  path('r/<slug>/', views.RView.as_view(), name='rdetail'),
                  path('csharp/', views.CSharpView.as_view(), name='csharp'),
                  path('csharp/<slug>/', views.CSharpView.as_view(), name='csharpdetail'),
                  path('swift/', views.SwiftView.as_view(), name='swift'),
                  path('swift/<slug>/', views.SwiftView.as_view(), name='swiftdetail'),
                  path('js/', views.JavaScriptView.as_view(), name='javascript'),
                  path('js/<slug>/', views.JavaScriptView.as_view(), name='javascriptdetail'),
                  path('js/', views.JavaScriptView.as_view(), name='js'),
                  path('js/<slug>/', views.JavaScriptView.as_view(), name='jsdetail'),
                  path('php/', views.PHPView.as_view(), name='php'),
                  path('php/<slug>/', views.PHPView.as_view(), name='phpdetail'),
                  path('dotnet/', views.DotNetView.as_view(), name='dotnet'),
                  path('dotnet/<slug>/', views.DotNetView.as_view(), name='dotnetdetail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
