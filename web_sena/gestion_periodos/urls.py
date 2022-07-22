from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('periodos/add/', views.addPeriodo, name="get"),
    path('periodos/update/<id>/', views.updatePeriodo, name="update"),
    path('periodos/delete/<id>/', views.deletePeriodo, name="delete"),
]