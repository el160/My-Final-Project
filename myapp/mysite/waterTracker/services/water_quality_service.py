"""Service layer for water quality operations."""

from django.contrib.auth.models import User
from ..models import WaterSource, WaterQualityData, Recommendation
from ..utils.water_safety import check_water_safety, generate_recommendation

class WaterQualityService:
    @staticmethod
    def create_water_source(name: str, location: str, latitude: float, 
                          longitude: float, user: User) -> WaterSource:
        """Create a new water source."""
        return WaterSource.objects.create(
            name=name,
            location=location,
            latitude=latitude,
            longitude=longitude,
            added_by=user
        )

    @staticmethod
    def record_quality_data(source: WaterSource, ph_level: float,
                          turbidity: float, contaminants: float,
                          notes: str, user: User) -> WaterQualityData:
        """Record new water quality data and generate recommendations if needed."""
        is_safe = check_water_safety(ph_level, turbidity, contaminants)
        
        quality_data = WaterQualityData.objects.create(
            source=source,
            ph_level=ph_level,
            turbidity=turbidity,
            contaminants=contaminants,
            is_safe=is_safe,
            notes=notes,
            recorded_by=user
        )

        if not is_safe:
            recommendation_text = generate_recommendation(ph_level, turbidity, contaminants)
            Recommendation.objects.create(
                quality_data=quality_data,
                treatment_method=recommendation_text
            )

        return quality_data