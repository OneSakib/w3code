from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Hosting'

urlpatterns = [
                  path('digitalocean/', views.DigitalOceanView.as_view(), name='digitalocean'),
                  path('digitalocean/<slug>/', views.DigitalOceanDetailView.as_view(), name='digitaloceandetail'),
                  path('msazure/', views.MSAzureView.as_view(), name='msazure'),
                  path('msazure/<slug>/', views.MSAzureDetailView.as_view(), name='msazuredetail'),
                  path('aws/', views.AWSView.as_view(), name='aws'),
                  path('aws/<slug>/', views.AWSDetailView.as_view(), name='awsdetail'),
                  path('pythonanywhere/', views.PythonAnywhereView.as_view(), name='pythonanywhere'),
                  path('pythonanywhere/<slug>/', views.PythonAnywhereDetailView.as_view(), name='pythonanywheredetail'),
                  path('herokuapp/', views.HerokuAppView.as_view(), name='herokuapp'),
                  path('herokuapp/<slug>/', views.HerokuAppDetailView.as_view(), name='herokuappdetail'),
                  path('githubhost/', views.GithubHostView.as_view(), name='githubhost'),
                  path('githubhost/<slug>/', views.GithubHostDetailView.as_view(), name='githubhostdetail'),
                  path('bluehost/', views.BlueHostView.as_view(), name='bluehost'),
                  path('bluehost/<slug>/', views.BlueHostDetailView.as_view(), name='bluehostdetail'),
                  path('hostgator/', views.HostGatorView.as_view(), name='hostgator'),
                  path('hostgator/<slug>/', views.HostGatorDetailView.as_view(), name='hostgatordetail'),
                  path('inmotionhosting/', views.InMotionHostingView.as_view(), name='inmotionhosting'),
                  path('inmotionhosting/<slug>/', views.InMotionHostingDetailView.as_view(), name='inmotionhostingdetail'),
                  path('a2hosting/', views.A2HostingView.as_view(), name='a2hosting'),
                  path('a2hosting/<slug>/', views.A2HostingDetailView.as_view(), name='a2hostingdetail'),
                  path('greengeeks/', views.GreenGeeksView.as_view(), name='greegeeks'),
                  path('greengeeks/<slug>/', views.GreenGeeksDetailView.as_view(), name='greengeeksdetail'),
                  path('hostinger/', views.HostingerView.as_view(), name='hostinger'),
                  path('hostinger/<slug>/', views.HostingerDetailView.as_view(), name='hostingerdetail'),
                  path('godaddy/', views.GoDaddyView.as_view(), name='godaddy'),
                  path('godaddy/<slug>/', views.GoDaddyDetailView.as_view(), name='godaddydetail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
