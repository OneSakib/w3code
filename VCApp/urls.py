from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'VC'

urlpatterns = [
                  path('docker/', views.DockerView.as_view(), name='docker'),
                  path('docker/<slug>/', views.DockerDetailView.as_view(), name='dockerdetail'),
                  path('git/', views.GitView.as_view(), name='git'),
                  path('git/<slug>/', views.GitDetailView.as_view(), name='gitdetail'),
                  path('github/', views.GithubView.as_view(), name='github'),
                  path('github/<slug>/', views.GitHubDetailView.as_view(), name='githubdetail'),

              ]
