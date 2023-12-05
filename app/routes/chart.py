from flask import Blueprint, render_template
import plotly.express as px
import pandas as pd
import numpy as np

# Create a Blueprint for chart-related routes
chart_bp = Blueprint('chart', __name__)

@chart_bp.route('/chart')
def show_chart():
    # Sample data for demonstration
    df = pd.DataFrame({
        'Date': pd.date_range(start='2020-01-01', periods=100),
        'Value': 100 + np.random.randn(100).cumsum()
    })

    # Create a Plotly figure
    fig = px.line(df, x='Date', y='Value', title='Sample Asset Price Over Time')

    # Convert to HTML
    graph_html = fig.to_html(full_html=False)

    return render_template('chart.html', graph_html=graph_html)
