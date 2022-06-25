from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Java'

urlpatterns = [
                  path('servlet/', views.ServletView.as_view(), name='servlet'),
                  path('servlet/<slug>/', views.ServletDetailView.as_view(), name='servletdetail'),
                  path('jsp/', views.JspView.as_view(), name='jsp'),
                  path('jsp/<slug>/', views.JSPDetailView.as_view(), name='jspdetail'),
                  path('springboot/', views.SpringBootView.as_view(), name='springboot'),
                  path('springboot/<slug>/', views.SpringBootDetailView.as_view(), name='springbootdetail'),
                  path('springframework/', views.SpringFrameworkView.as_view(), name='springframework'),
                  path('springframework/<slug>/', views.SpringFrameworkDetailView.as_view(),
                       name='springframeworkdetail'),
                  path('hibernate/', views.HibernateView.as_view(), name='hibernate'),
                  path('hibernate/<slug>/', views.HibernateDetailView.as_view(), name='hibernatedetail'),
                  path('javaswing/', views.JavaSwingView.as_view(), name='javaswing'),
                  path('javaswing/<slug>/', views.JavaSwingDetailView.as_view(), name='javaswingdetail'),
                  path('javafx/', views.JavaFXView.as_view(), name='javafx'),
                  path('javafx/<slug>/', views.JavaFxDetailView.as_view(), name='javafxdetail'),
                  path('javaawt/', views.JavaAWTView.as_view(), name='javaawt'),
                  path('javaawt/<slug>/', views.JavaAWTDetailView.as_view(), name='javaawtdetail'),
                  path('javacollections/', views.JavaCollectionsView.as_view(), name='javacollections'),
                  path('javacollections/<slug>/', views.JavaCollectionsDetailView.as_view(),
                       name='javacollectionsdetail'),
                  path('javadate/', views.JavaDateView.as_view(), name='javadate'),
                  path('javadate/<slug>/', views.JavaDateDetailView.as_view(), name='javadatedetail'),
                  path('javaio/', views.JavaIOView.as_view(), name='javaio'),
                  path('javaio/<slug>/', views.JavaIODetailView.as_view(), name='javaiodetail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
