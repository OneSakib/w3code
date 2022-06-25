from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'MS'

urlpatterns = [
                  path('msword/', views.MSWordView.as_view(), name='msword'),
                  path('msword/<slug>/', views.MSWordDetailView.as_view(), name='msworddetail'),
                  path('msexcel/', views.MSExcelView.as_view(), name='msexcel'),
                  path('msexcel/<slug>/', views.MSExcelDetailView.as_view(), name='msexceldetail'),
                  path('mspowerpoint/', views.MSPowerpointView.as_view(), name='mspowerpoint'),
                  path('mspowerpoint/<slug>/', views.MSPowerpointDetailView.as_view(), name='mspowerpointdetail'),
                  path('msonenote/', views.MSOneNoteView.as_view(), name='msonenote'),
                  path('msonenote/<slug>/', views.MSOneNoteDetailView.as_view(), name='msonenotedetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
