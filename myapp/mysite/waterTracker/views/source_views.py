"""
Views for managing water sources.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import WaterSourceForm
from ..models import WaterSource
from ..services.water_quality_service import WaterQualityService

@login_required
def add_source(request):
    """Add a new water source."""
    if request.method == 'POST':
        form = WaterSourceForm(request.POST)
        if form.is_valid():
            WaterQualityService.create_water_source(
                name=form.cleaned_data['name'],
                location=form.cleaned_data['location'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
                user=request.user
            )
            messages.success(request, 'Water source added successfully!')
            return redirect('water_quality:dashboard')
    else:
        form = WaterSourceForm()
    return render(request, 'water_quality/add_source.html', {'form': form})

@login_required
def source_detail(request, pk):
    """Display details of a specific water source."""
    source = get_object_or_404(WaterSource, pk=pk, added_by=request.user)
    return render(request, 'water_quality/source_detail.html', {'source': source})

@login_required
def source_list(request):
    """Display list of all water sources."""
    sources = WaterSource.objects.filter(added_by=request.user)
    return render(request, 'water_quality/source_list.html', {'sources': sources})