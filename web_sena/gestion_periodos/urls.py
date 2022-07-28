from urllib.parse import urlparse
from django.urls import path,include
from . import views

urlpatterns = [
    path('periodos/', views.home, name="periodos"),
    path('periodos/add/', views.addPeriodo, name="get"),
    path('periodos/update/<id>/', views.updatePeriodo, name="update"),
    path('periodos/delete/<id>/', views.deletePeriodo, name="delete"),
]