from urllib.parse import urlparse
from django.urls import path,include
from . import views

urlpatterns = [
    path('ambientes/', views.home, name="ambientes"),
    path('ambientes/add/', views.addAmbiente, name="get"),
    path('ambientes/update/<id>/', views.updateAmbiente, name="update"),
    path('ambientes/delete/<id>/', views.deleteAmbiente, name="delete"),
]