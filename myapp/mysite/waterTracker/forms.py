from django import forms
from .models import WaterSource, WaterQualityData

class WaterSourceForm(forms.ModelForm):
    class Meta:
        model = WaterSource
        fields = ['name', 'location', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }

class WaterQualityDataForm(forms.ModelForm):
    class Meta:
        model = WaterQualityData
        fields = ['source', 'ph_level', 'turbidity', 'contaminants', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }