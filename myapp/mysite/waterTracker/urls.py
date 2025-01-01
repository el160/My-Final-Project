"""
URL patterns for the water_quality app.
"""
from django.urls import path
from .views import home_views, dashboard_views, source_views, quality_views

app_name = 'WaterTracker'

urlpatterns = [
    # Home
    path('', home_views.home, name='home'),
    
    # Dashboard
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    
    # Water Sources
    path('sources/add/', source_views.add_source, name='add_source'),
    path('sources/<int:pk>/', source_views.source_detail, name='source_detail'),
    path('sources/', source_views.source_list, name='source_list'),
    
    # Water Quality Data
    path('quality/add/', quality_views.add_quality_data, name='add_quality_data'),
    path('quality/<int:pk>/', quality_views.quality_detail, name='quality_detail'),
    path('quality/', quality_views.quality_list, name='quality_list'),
]