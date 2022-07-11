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
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='loginuser'),
    path('logout/', views.UserLogout.as_view(), name='logoutuser'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('savedarticle/', views.UserSaveArticle.as_view(), name='savedarticle'),
    path('profileupdate/', views.UserProfileUpdate.as_view(), name='profileupdate'),
    path('bookmark/', views.Bookmark.as_view(), name='bookmark'),
    path('upload_image/', views.ImageUpload.as_view(), name='upload_image'),
    path('verify/<key>/', views.VerifyAccount.as_view(), name='account_verification'),
    path('contactus/', views.ContactUsView.as_view(), name='contact_us'),
    path('aboutus/', views.AboutUsView.as_view(), name='about_us'),
    path("password_reset/", views.PasswordResetRequest.as_view(), name="password_reset"),
    path('privacypolicy/', views.PrivacyPolicyView.as_view(), name='privacypolicy'),
    path('author/<name>/', views.AuthorView.as_view(), name='author')
]
