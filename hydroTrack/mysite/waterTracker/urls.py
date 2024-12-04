from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-source/', views.add_source, name='add_source'),
    path('add-quality-data/', views.add_quality_data, name='add_quality_data'),
]