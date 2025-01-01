"""Views for the home page."""

from django.shortcuts import render

def home(request):
    """Display the home page."""
    return render(request, 'water_quality/home.html')