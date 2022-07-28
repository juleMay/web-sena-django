from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('horario/', views.horario, name="horario"),
    path('perfil/', views.perfil, name="perfil"),
]