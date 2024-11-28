from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import WaterSource
from .analysis import analyze_water, recommend_actions

def home_screen(request):
    print(request.headers)
    return render (request, 'tracker/home.html',{})



def home(request):
    if request.method == "POST":
        location = request.POST['location']
        ph = float(request.POST['ph'])
        turbidity = float(request.POST['turbidity'])
        contaminants = float(request.POST['contaminants'])

        status, issues = analyze_water(ph, turbidity, contaminants)
        recommendations = recommend_actions(issues)

        WaterSource.objects.create(
            location=location, ph=ph, turbidity=turbidity, 
            contaminants=contaminants, status=status
        )

        return render(request, "tracker/home.html", {
            "status": status,
            "issues": issues,
            "recommendations": recommendations
        })

    return render(request, "home.html")

def trends(request):
    data = WaterSource.objects.all()
    return render(request, "trends.html", {"data": data})
