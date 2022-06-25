from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'JavaScript'

urlpatterns = [

                  path('jquery/', views.JqueryView.as_view(), name='jquery'),
                  path('jquery/<slug>/', views.JqueryDetailView.as_view(), name='jquerydetail'),
                  path('angularjs/', views.AngularView.as_view(), name='angular'),
                  path('angularjs/<slug>/', views.AngularDetailView.as_view(), name='angulardetail'),
                  path('nodejs/', views.NodejsView.as_view(), name='nodejs'),
                  path('nodejs/<slug>/', views.NodejsDetailView.as_view(), name='nodejsdetail'),
                  path('expressjs/', views.ExpressjsView.as_view(), name='expressjs'),
                  path('expressjs/<slug>/', views.ExpressjsDetailView.as_view(), name='expressjsdetail'),
                  path('reactjs/', views.ReactjsView.as_view(), name='reactjs'),
                  path('reactjs/<slug>/', views.ReactjsDetailView.as_view(), name='reactjsdetail'),
                  path('typescript/', views.TypescriptView.as_view(), name='typescript'),
                  path('typescript/<slug>/', views.TypescriptDetailView.as_view(), name='typescriptdetail'),
                  path('vuejs/', views.VuejsView.as_view(), name='vuejs'),
                  path('vuejs/<slug>/', views.VuejsDetailView.as_view(), name='vuejsdetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
