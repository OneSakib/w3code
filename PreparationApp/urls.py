from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Preparation'

urlpatterns = [

                  path('aptitude/', views.AptitudeView.as_view(), name='aptitude'),
                  path('aptitude/<slug>/', views.AptitudeView.as_view(), name='aptitudedetail'),
                  path('reasoning/', views.ReasoningView.as_view(), name='reasoning'),
                  path('reasoning/<slug>/', views.ReasoningView.as_view(), name='reasoningdetail'),
                  path('verbalability/', views.VerbalAbilityView.as_view(), name='verbalability'),
                  path('verbalability/<slug>/', views.VerbalAbilityView.as_view(), name='verbalabilitydetail'),
                  path('interviewquestion/', views.InterViewQuestionView.as_view(), name='interviewquestion'),
                  path('interviewquestion/<slug>/', views.InterViewQuestionView.as_view(),
                       name='interviewquestiondetail'),
                  path('companyquestion/', views.CompanyQuestionView.as_view(), name='companyquestion'),
                  path('companyquestion/<slug>/', views.CompanyQuestionView.as_view(), name='companyquestiondetail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
