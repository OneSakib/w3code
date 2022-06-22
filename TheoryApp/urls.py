from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Theory'

urlpatterns = [

                  path('dbms/', views.DBMSView.as_view(), name='dbms'),
                  path('dbms/<slug>/', views.DBMSView.as_view(), name='dbmsdetail'),
                  path('datastructure/', views.DataStructureView.as_view(), name='datastructure'),
                  path('datastructure/<slug>/', views.DataStructureView.as_view(), name='datastructuredetail'),
                  path('daa/', views.DAAView.as_view(), name='daa'),
                  path('daa/<slug>/', views.DAAView.as_view(), name='daadetail'),
                  path('operatingsystem/', views.OperatingSystemView.as_view(), name='operatingsystem'),
                  path('operatingsystem/<slug>/', views.OperatingSystemView.as_view(), name='operatingsystemdetail'),
                  path('computernetwork/', views.ComputeNetworkView.as_view(), name='computernetwork'),
                  path('computernetwork/<slug>/', views.ComputeNetworkView.as_view(), name='computernetworkdetail'),
                  path('compilerdesign/', views.CompilerDesignView.as_view(), name='compilerdesign'),
                  path('compilerdesign/<slug>/', views.CompilerDesignView.as_view(), name='compilerdesigndetail'),
                  path('computerorganization/', views.ComputerOrganizationView.as_view(), name='computerorganization'),
                  path('computerorganization/<slug>/', views.ComputerOrganizationView.as_view(),
                       name='computerorganizationdetail'),
                  path('discretemathematics/', views.DiscreteMathematicsView.as_view(), name='discretemathematics'),
                  path('discretemathematics/<slug>/', views.DiscreteMathematicsView.as_view(),
                       name='discretemathematicsdetail'),
                  path('softwareengineering/', views.SoftwareEngineeringView.as_view(), name='softwareengineering'),
                  path('softwareengineering/<slug>/', views.SoftwareEngineeringView.as_view(),
                       name='softwareengineeringdetail'),
                  path('cybersecurity/', views.CyberSecurityView.as_view(), name='cybersecurity'),
                  path('cybersecurity/<slug>/', views.CyberSecurityView.as_view(), name='cybersecuritydetail'),
                  path('datamininganddatawarehouse/', views.DataMiningView.as_view(),
                       name='datamininganddatawarehouse'),
                  path('datamininganddatawarehouse/<slug>/', views.DataMiningView.as_view(),
                       name='datamininganddatawarehousedetail'),
                  path('artificialintelligence/', views.ArtificialIntelligenceView.as_view(),
                       name='artificialintelligence'),
                  path('artificialintelligence/<slug>/', views.ArtificialIntelligenceView.as_view(),
                       name='artificialintelligencedetail'),
                  path('automata/', views.AutomataView.as_view(), name='automata'),
                  path('automata/<slug>/', views.AutomataView.as_view(), name='automatadetail'),
                  path('computergraphics/', views.ComputerGraphicsView.as_view(), name='computergraphics'),
                  path('computergraphics/<slug>/', views.ComputerGraphicsView.as_view(), name='computergraphicsdetail'),
                  path('webapi/', views.WebApiView.as_view(), name='webapi'),
                  path('webapi/<slug>/', views.WebApiView.as_view(), name='webapidetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
