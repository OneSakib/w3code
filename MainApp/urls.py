from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

app_name = 'w3c'

urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
                  path('onlineide/<str:slug>/', views.OnlineCompiler, name='onlineide'),
                  path('blog/', views.BlogView.as_view(), name='blog'),
                  path('blog/<slug>/', views.BlogDetailView.as_view(), name='blogdetail'),
                  path('comments/', views.CommentsView.as_view(), name='comments'),
                  path('comments/<slug>/', views.CommentsDetailView.as_view(), name='commentsdetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
