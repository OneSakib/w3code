from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Database'

urlpatterns = [
                  path('mysql/', views.MYSqlView.as_view(), name='mysql'),
                  path('mysql/<slug>/', views.MySqlDetailView.as_view(), name='mysqldetail'),
                  path('mongodb/', views.MongoDBView.as_view(), name='mongodb'),
                  path('mongodb/<slug>/', views.MongoDBDetailView.as_view(), name='mongodbdetail'),
                  path('postgresql/', views.PostgreSqlView.as_view(), name='postgresql'),
                  path('postgresql/<slug>/', views.PostgreSQLDetailView.as_view(), name='postgresqldetail'),
                  path('oracle/', views.OracleView.as_view(), name='oracle'),
                  path('oracle/<slug>/', views.OracleDetailView.as_view(), name='oracledetail'),
                  path('sqlite/', views.SqliteView.as_view(), name='sqlite'),
                  path('sqlite/<slug>/', views.SqliteDetailView.as_view(), name='sqlitedetail'),
                  path('mariadb/', views.MariaDBView.as_view(), name='mariadbd'),
                  path('mariadb/<slug>/', views.MariaDBDetailView.as_view(), name='mariadbddetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
