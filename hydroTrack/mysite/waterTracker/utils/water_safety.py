"""Utility functions for water safety calculations."""

def check_water_safety(ph_level: float, turbidity: float, contaminants: float) -> bool:
    """
    Check if water parameters are within WHO safe ranges.
    """
    return (
        6.5 <= ph_level <= 8.5 and
        turbidity <= 5 and
        contaminants <= 0.5
    )

def generate_recommendation(ph_level: float, turbidity: float, contaminants: float) -> str:
    """
    Generate treatment recommendations based on water parameters.
    """
    recommendations = []
    
    if ph_level < 6.5:
        recommendations.append("Add lime or baking soda to increase pH level.")
    elif ph_level > 8.5:
        recommendations.append("Add vinegar or citric acid to decrease pH level.")
    
    if turbidity > 5:
        recommendations.append("Use filtration methods like sand filtration or cloth filtration.")
    
    if contaminants > 0.5:
        recommendations.append("Boil water for at least 5 minutes. Consider using water purification tablets.")
    
    return " ".join(recommendations) if recommendations else "No specific treatment needed."