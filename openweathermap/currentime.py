import requests
from datetime import datetime, timedelta
from pytz import timezone
from utils.CONFIG import API_KEY

def format_unix_timestamp(timestamp, city_timezone):
    # Convertit le timestamp UNIX en format de date "16/07/2024 HH:mm"
    local_time = datetime.utcfromtimestamp(timestamp) + timedelta(seconds=city_timezone)
    return local_time.strftime('%d/%m/%Y %H:%M')

def get_actual_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Récupère le décalage horaire de la ville en secondes
        city_timezone = data['timezone']
        
        # Formater les dates si elles sont présentes dans les données
        if 'dt' in data:
            data['dt'] = format_unix_timestamp(data['dt'], city_timezone)
        
        if 'sys' in data and 'sunrise' in data['sys']:
            data['sys']['sunrise'] = format_unix_timestamp(data['sys']['sunrise'], city_timezone)
        
        if 'sys' in data and 'sunset' in data['sys']:
            data['sys']['sunset'] = format_unix_timestamp(data['sys']['sunset'], city_timezone)
        
        return data  # Retourne l'objet JSON complet avec les dates formatées
        
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    city_name = "Nantes"  # Remplacé "Rennes" par "Nantes" selon votre exemple
    
    weather_data = get_actual_weather(city_name)
    
    if weather_data:
        print("Données météo pour Nantes:")
        print(weather_data)
    else:
        print("Échec de la récupération des données météo.")
