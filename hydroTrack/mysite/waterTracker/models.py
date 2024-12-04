from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class WaterSource(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WaterQualityData(models.Model):
    source = models.ForeignKey(WaterSource, on_delete=models.CASCADE)
    recorded_date = models.DateTimeField(auto_now_add=True)
    ph_level = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(14)],
        verbose_name="pH Level"
    )
    turbidity = models.FloatField(validators=[MinValueValidator(0)])
    contaminants = models.FloatField(validators=[MinValueValidator(0)])
    is_safe = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Check if water is safe based on WHO standards
        self.is_safe = (
            6.5 <= self.ph_level <= 8.5 and
            self.turbidity <= 5 and
            self.contaminants <= 0.5
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.source.name} - {self.recorded_date.date()}"

class Recommendation(models.Model):
    quality_data = models.OneToOneField(WaterQualityData, on_delete=models.CASCADE)
    treatment_method = models.TextField()
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.quality_data.source.name}"
