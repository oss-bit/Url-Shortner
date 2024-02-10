from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('profile/', views.renderProfile, name='profile'),
    path('profile/generate/', views.ajax_url, name='ajax_url'),
    path('<str:url>', views.tempRedirect, name='temp_redirect'),
]
