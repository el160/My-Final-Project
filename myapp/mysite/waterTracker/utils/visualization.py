"""Utility functions for data visualization."""

import plotly.express as px
import pandas as pd
from typing import Optional

def create_ph_trend_plot(data_values: list) -> Optional[str]:
    """
    Create a pH trend visualization using plotly.
    """
    if not data_values:
        return None
        
    df = pd.DataFrame(data_values)
    fig = px.line(
        df, 
        x='recorded_date', 
        y='ph_level', 
        title='pH Levels Over Time',
        labels={'ph_level': 'pH Level', 'recorded_date': 'Date'}
    )
    return fig.to_html(full_html=False)