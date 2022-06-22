from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'JavaScript'

urlpatterns = [

                  path('jquery/', views.JqueryView.as_view(), name='jquery'),
                  path('jquery/<slug>/', views.JqueryView.as_view(), name='jquerydetail'),
                  path('angular/', views.AngularView.as_view(), name='angular'),
                  path('angular/<slug>/', views.AngularView.as_view(), name='angulardetail'),
                  path('nodejs/', views.NodejsView.as_view(), name='nodejs'),
                  path('nodejs/<slug>/', views.NodejsView.as_view(), name='nodejsdetail'),
                  path('expressjs/', views.ExpressjsView.as_view(), name='expressjs'),
                  path('expressjs/<slug>/', views.ExpressjsView.as_view(), name='expressjsdetail'),
                  path('reactjs/', views.ReactjsView.as_view(), name='reactjs'),
                  path('reactjs/<slug>/', views.ReactjsView.as_view(), name='reactjsdetail'),
                  path('typescript/', views.TypescriptView.as_view(), name='typescript'),
                  path('typescript/<slug>/', views.TypescriptView.as_view(), name='typescriptdetail'),
                  path('vuejs/', views.VuejsView.as_view(), name='vuejs'),
                  path('vuejs/<slug>/', views.VuejsView.as_view(), name='vuejsdetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
