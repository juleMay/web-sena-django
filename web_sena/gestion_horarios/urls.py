from urllib.parse import urlparse
from django.urls import path,include
from . import views

urlpatterns = [
    path('horarios/', views.home, name="horarios"),
    path('horarios/add/', views.addHorario, name="get"),
    path('horarios/update/<id>/', views.updateHorario, name="update"),
    path('horarios/delete/<id>/', views.deleteHorario, name="delete"),
]