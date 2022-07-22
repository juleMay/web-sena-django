from urllib.parse import urlparse
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registerView,  name="register"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutRequest, name="logout"),
]