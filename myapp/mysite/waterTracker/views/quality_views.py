"""Views for managing water quality data."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import WaterQualityDataForm
from ..services.water_quality_service import WaterQualityService

@login_required
def add_quality_data(request):
    """Record new water quality data."""
    if request.method == 'POST':
        form = WaterQualityDataForm(request.POST)
        if form.is_valid():
            WaterQualityService.record_quality_data(
                source=form.cleaned_data['source'],
                ph_level=form.cleaned_data['ph_level'],
                turbidity=form.cleaned_data['turbidity'],
                contaminants=form.cleaned_data['contaminants'],
                notes=form.cleaned_data['notes'],
                user=request.user
            )
            messages.success(request, 'Water quality data recorded successfully!')
            return redirect('dashboard')
    else:
        form = WaterQualityDataForm()
    return render(request, 'water_quality/add_quality_data.html', {'form': form})