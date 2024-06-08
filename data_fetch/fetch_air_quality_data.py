import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

# Getting the AirQuality API key from environment variables
API_KEY = os.getenv('AIRQUALITY_API_KEY')

# List of cities for which air quality data will be fetched
CITIES = ["London", "New York", "Tokyo", "Sydney", "Mumbai"]

def fetch_airquality_data(city):
    """
    Fetches air quality data for a given city from the AirQuality API.

    Args:
        city (str): The name of the city for which air quality data is to be fetched.

    Returns:
        dict: A dictionary containing relevant air quality data for the city.
    """
    # Constructing the URL for AirQuality API call
    url = f"https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality?city={city}"
    # Setting headers with API key
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "air-quality-by-api-ninjas.p.rapidapi.com"
    }
    # Sending HTTP GET request to the API
    response = requests.get(url, headers=headers)
    # Parsing JSON response
    data = response.json()
    print('data', data)
    # Returning a dictionary containing relevant air quality data for the city
    return {
        "city": city,
        "overall_aqi": data["overall_aqi"],
        "date": datetime.now().strftime('%Y-%m-%d'),  # Current date
        "time": datetime.now().strftime('%H:%M:%S')   # Current time
    }

def main():
    """
    Main function to fetch air quality data for multiple cities and store it in a PostgreSQL database.
    """
    # Fetching air quality data for all cities in the list
    airquality_data = [fetch_airquality_data(city) for city in CITIES]
    # Creating a DataFrame from the fetched data
    df = pd.DataFrame(airquality_data)
    # Creating a SQLAlchemy engine to connect to the PostgreSQL database
    engine = create_engine('postgresql://postgres:password@database:5432/airquality_db')
    # Writing the DataFrame to the database table 'airquality_data'
    # if_exists='append' specifies that if the table exists, data will be appended to it
    df.to_sql('airquality_data', engine, if_exists='append', index=False)

# Entry point of the script
if __name__ == "__main__":
    main()  # Calling the main function when the script is executed directly
