from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'w3c'

urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
