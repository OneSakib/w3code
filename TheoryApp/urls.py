from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Theory'

urlpatterns = [

                  path('dbms/', views.DBMSView.as_view(), name='dbms'),
                  path('dbms/<slug>/', views.DBMSDetailView.as_view(), name='dbmsdetail'),
                  path('datastructure/', views.DataStructureView.as_view(), name='datastructure'),
                  path('datastructure/<slug>/', views.DataStructureDetailView.as_view(), name='datastructuredetail'),
                  path('daa/', views.DAAView.as_view(), name='daa'),
                  path('daa/<slug>/', views.DAADetailView.as_view(), name='daadetail'),
                  path('operatingsystem/', views.OperatingSystemView.as_view(), name='operatingsystem'),
                  path('operatingsystem/<slug>/', views.OperatingSystemDetailView.as_view(),
                       name='operatingsystemdetail'),
                  path('computernetwork/', views.ComputeNetworkView.as_view(), name='computernetwork'),
                  path('computernetwork/<slug>/', views.ComputerNetworkDetailView.as_view(),
                       name='computernetworkdetail'),
                  path('compilerdesign/', views.CompilerDesignView.as_view(), name='compilerdesign'),
                  path('compilerdesign/<slug>/', views.CompilerDesignDetailView.as_view(), name='compilerdesigndetail'),
                  path('computerorganization/', views.ComputerOrganizationView.as_view(), name='computerorganization'),
                  path('computerorganization/<slug>/', views.ComputerOrganizationDetailView.as_view(),
                       name='computerorganizationdetail'),
                  path('discretemathematics/', views.DiscreteMathematicsView.as_view(), name='discretemathematics'),
                  path('discretemathematics/<slug>/', views.DiscreteMathematicsDetailView.as_view(),
                       name='discretemathematicsdetail'),
                  path('softwareengineering/', views.SoftwareEngineeringView.as_view(), name='softwareengineering'),
                  path('softwareengineering/<slug>/', views.SoftwareEngineeringDetailView.as_view(),
                       name='softwareengineeringdetail'),
                  path('cybersecurity/', views.CyberSecurityView.as_view(), name='cybersecurity'),
                  path('cybersecurity/<slug>/', views.CyberSecurityDetailView.as_view(), name='cybersecuritydetail'),
                  path('datamininganddatawarehouse/', views.DataMiningView.as_view(),
                       name='datamininganddatawarehouse'),
                  path('datamininganddatawarehouse/<slug>/', views.DataMiningDetailView.as_view(),
                       name='datamininganddatawarehousedetail'),
                  path('artificialintelligence/', views.ArtificialIntelligenceView.as_view(),
                       name='artificialintelligence'),
                  path('artificialintelligence/<slug>/', views.ArtificialIntelligenceDetailView.as_view(),
                       name='artificialintelligencedetail'),
                  path('automatatheory/', views.AutomataView.as_view(), name='automata'),
                  path('automatatheory/<slug>/', views.AutomataDetailView.as_view(), name='automatadetail'),
                  path('computergraphics/', views.ComputerGraphicsView.as_view(), name='computergraphics'),
                  path('computergraphics/<slug>/', views.ComputerGraphicsDetailView.as_view(),
                       name='computergraphicsdetail'),
                  path('webapi/', views.WebApiView.as_view(), name='webapi'),
                  path('webapi/<slug>/', views.WebAPIDetailView.as_view(), name='webapidetail'),
                  path('ddbms/', views.DDBMSView.as_view(), name='ddbms'),
                  path('ddbms/<slug>/', views.DDBMSDetailView.as_view(), name='ddbmsdetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
