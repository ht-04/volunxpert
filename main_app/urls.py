from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Root URL -> landing page
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
