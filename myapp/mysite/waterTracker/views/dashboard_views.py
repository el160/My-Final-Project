"""Views for the dashboard functionality."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import WaterSource, WaterQualityData
from ..utils.visualization import create_ph_trend_plot

@login_required
def dashboard(request):
    """Display the user's dashboard with water quality data and visualizations."""
    sources = WaterSource.objects.filter(added_by=request.user)
    recent_data = WaterQualityData.objects.filter(
        recorded_by=request.user
    ).order_by('-recorded_date')[:5]
    
    plot_div = create_ph_trend_plot(list(recent_data.values()))

    context = {
        'sources': sources,
        'recent_data': recent_data,
        'plot_div': plot_div,
    }
    return render(request, 'water_quality/dashboard.html', context)