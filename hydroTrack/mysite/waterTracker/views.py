from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WaterSource, WaterQualityData, Recommendation
from .forms import WaterSourceForm, WaterQualityDataForm
import plotly.express as px
import pandas as pd

def home(request):
    return render(request, 'water_quality/home.html')

@login_required
def dashboard(request):
    sources = WaterSource.objects.filter(added_by=request.user)
    recent_data = WaterQualityData.objects.filter(
        recorded_by=request.user
    ).order_by('-recorded_date')[:5]
    
    # Create visualization data
    if recent_data:
        df = pd.DataFrame(list(recent_data.values()))
        fig = px.line(df, x='recorded_date', y='ph_level', title='pH Levels Over Time')
        plot_div = fig.to_html(full_html=False)
    else:
        plot_div = None

    context = {
        'sources': sources,
        'recent_data': recent_data,
        'plot_div': plot_div,
    }
    return render(request, 'water_quality/dashboard.html', context)

@login_required
def add_source(request):
    if request.method == 'POST':
        form = WaterSourceForm(request.POST)
        if form.is_valid():
            source = form.save(commit=False)
            source.added_by = request.user
            source.save()
            messages.success(request, 'Water source added successfully!')
            return redirect('dashboard')
    else:
        form = WaterSourceForm()
    return render(request, 'water_quality/add_source.html', {'form': form})

@login_required
def add_quality_data(request):
    if request.method == 'POST':
        form = WaterQualityDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.recorded_by = request.user
            data.save()
            
            # Generate recommendation
            if not data.is_safe:
                recommendation_text = generate_recommendation(data)
                Recommendation.objects.create(
                    quality_data=data,
                    treatment_method=recommendation_text
                )
            
            messages.success(request, 'Water quality data recorded successfully!')
            return redirect('dashboard')
    else:
        form = WaterQualityDataForm()
    return render(request, 'water_quality/add_quality_data.html', {'form': form})

def generate_recommendation(data):
    recommendation = []
    
    if data.ph_level < 6.5:
        recommendation.append("Add lime or baking soda to increase pH level.")
    elif data.ph_level > 8.5:
        recommendation.append("Add vinegar or citric acid to decrease pH level.")
    
    if data.turbidity > 5:
        recommendation.append("Use filtration methods like sand filtration or cloth filtration.")
    
    if data.contaminants > 0.5:
        recommendation.append("Boil water for at least 5 minutes. Consider using water purification tablets.")
    
    return " ".join(recommendation) if recommendation else "No specific treatment needed."