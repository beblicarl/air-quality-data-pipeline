import requests
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import os

def get_airquality(api_key, city):
    # Base URL for AirQuality API
    base_url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
    
    # Parameters for the API call
    params = {
        'city': city
    }
    api_key = os.getenv('AIRQUALITY_API_KEY')
    # Headers with API key
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "air-quality-by-api-ninjas.p.rapidapi.com"
    }
    
    # Make a GET request to the API
    response = requests.get(base_url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        
        # Extract relevant information
        airquality = {
            'city': city,
            'overall_aqi': data['overall_aqi'],
            'date': datetime.now().strftime('%Y-%m-%d'),  # Current date
            'time': datetime.now().strftime('%H:%M:%S')   # Current time
        }
        
        return airquality
    else:
        # Handle errors
        return {'error': f"Failed to get air quality data for {city}"}

# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'  # Replace with your actual API key
cities = ["London", "New York", "Tokyo", "Sydney", "Mumbai"]

# Get air quality data for all cities
airquality_data_list = []
for city in cities:
    airquality_data = get_airquality(api_key, city)
    airquality_data_list.append(airquality_data)

# Convert the list of dictionaries to a DataFrame
airquality_df = pd.DataFrame(airquality_data_list)

# Plotly Interactive Visualizations

# Overall AQI by City
fig_aqi = px.bar(airquality_df, x='city', y='overall_aqi', title='Overall AQI by City',
                 labels={'overall_aqi': 'Overall AQI'}, 
                 hover_data={'overall_aqi': ':.2f'})
fig_aqi.update_traces(marker_color='skyblue')
fig_aqi.update_layout(xaxis_title='City', yaxis_title='Overall AQI')

# Enhanced Visualization using Seaborn and Matplotlib
def seaborn_visualizations(airquality_df):
    plt.figure(figsize=(10, 6))

    # Overall AQI plot
    sns.barplot(x='city', y='overall_aqi', data=airquality_df)
    plt.title('Overall AQI by City')
    plt.xlabel('City')
    plt.ylabel('Overall AQI')

    plt.tight_layout()
    plt.savefig('seaborn_visualization.png')  # Save Seaborn visualization as PNG

# Line Plot for Overall AQI over Time
fig_line = px.line(airquality_df, x='date', y='overall_aqi', color='city', title='Overall AQI over Time')
fig_line.update_layout(xaxis_title='Date', yaxis_title='Overall AQI')

# Box Plot for Overall AQI Distribution
fig_box = px.box(airquality_df, x='city', y='overall_aqi', title='Overall AQI Distribution')
fig_box.update_layout(xaxis_title='City', yaxis_title='Overall AQI')

# Histogram of Overall AQI
fig_hist = px.histogram(airquality_df, x='overall_aqi', title='Histogram of Overall AQI')
fig_hist.update_layout(xaxis_title='Overall AQI', yaxis_title='Frequency')

# Pie Chart for Overall AQI Proportions
fig_pie = px.pie(airquality_df, values='overall_aqi', names='city', title='Overall AQI Proportions')

# Save all plots as images
fig_line.write_image('line_plot.png')
fig_box.write_image('box_plot.png')
fig_hist.write_image('histogram.png')
fig_pie.write_image('pie_chart.png')

# Display the visualization
fig_aqi.show()

# Call the function to generate Seaborn visualizations
seaborn_visualizations(airquality_df)
