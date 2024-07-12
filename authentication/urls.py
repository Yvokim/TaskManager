from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='authentication/password_change_done'),
         name='password_change_done'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('profile/', views.profile, name='profile')
]


