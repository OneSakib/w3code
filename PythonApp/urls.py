from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Python'

urlpatterns = [
                  path('django/', views.DjangoView.as_view(), name='django'),
                  path('django/<slug>/', views.DjangoView.as_view(), name='djangodetail'),
                  path('flask/', views.FlaskView.as_view(), name='flask'),
                  path('flask/<slug>/', views.FlaskView.as_view(), name='flaskdetail'),
                  path('machinelearning/', views.MachineLearningView.as_view(), name='machinelearning'),
                  path('machinelearning/<slug>/', views.MachineLearningView.as_view(), name='machinelearningdetail'),
                  path('numpy/', views.NumpyView.as_view(), name='numpy'),
                  path('numpy/<slug>/', views.NumpyView.as_view(), name='numpydetail'),
                  path('tkinter/', views.TkinterView.as_view(), name='tkinter'),
                  path('tkinter/<slug>/', views.TkinterView.as_view(), name='tkinterdetail'),
                  path('pytorch/', views.PytorchView.as_view(), name='pytorch'),
                  path('pytorch/<slug>/', views.PytorchView.as_view(), name='pytorchdetail'),
                  path('pygame/', views.PygameView.as_view(), name='pygame'),
                  path('pygame/<slug>/', views.PygameView.as_view(), name='pygamedetail'),
                  path('scipy/', views.ScipyView.as_view(), name='scipy'),
                  path('scipy/<slug>/', views.ScipyView.as_view(), name='scipydetail'),
                  path('pandas/', views.PandasView.as_view(), name='pandas'),
                  path('pandas/<slug>/', views.PandasView.as_view(), name='pandasdetail'),
                  path('opencv/', views.OpenCVView.as_view(), name='opencv'),
                  path('opencv/<slug>/', views.OpenCVView.as_view(), name='opencvdetail'),
                  path('matplotlib/', views.MatplotlibView.as_view(), name='matplotlib'),
                  path('matplotlib/<slug>/', views.MatplotlibView.as_view(), name='matplotlibdetail'),
                  path('selenium/', views.SeleniumView.as_view(), name='selenium'),
                  path('selenium/<slug>/', views.SeleniumView.as_view(), name='seleniumdetail'),
                  path('kivy/', views.KivyView.as_view(), name='kivy'),
                  path('kivy/<slug>/', views.KivyView.as_view(), name='kivydetail'),
                  path('jupyter/', views.JupyterView.as_view(), name='jupyter'),
                  path('jupyter/<slug>/', views.JupyterView.as_view(), name='jupyterdetail'),
                  path('datascience/', views.DataScienceView.as_view(), name='datascience'),
                  path('datascience/<slug>/', views.DataScienceView.as_view(), name='datasciencedetail'),
                  path('deeplearning/', views.DeepLearningView.as_view(), name='deeplearning'),
                  path('deeplearning/<slug>/', views.DeepLearningView.as_view(), name='deeplearningdetail'),
                  path('pillow/', views.PillowView.as_view(), name='pillow'),
                  path('pillow/<slug>/', views.PillowView.as_view(), name='pillowdetail'),
                  path('tensorflow/', views.TensorflowView.as_view(), name='tensorflow'),
                  path('tensorflow/<slug>/', views.TensorflowView.as_view(), name='tensorflowdetail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
