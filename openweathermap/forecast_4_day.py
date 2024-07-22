import requests
from utils.CONFIG import API_KEY
from datetime import datetime, timedelta, timezone


def get_forecast_weather(city_name):
    # URL de l'API de prévision à 5 jours/3 heures
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    # city_timezone = data['timezone']
    # Vérifiez que la requête a réussi
    if response.status_code == 200:
        data = response.json()
      
        return data
    
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    city_name = "Nantes"
    
    weather_df = get_forecast_weather(city_name)
    
    print(weather_df)