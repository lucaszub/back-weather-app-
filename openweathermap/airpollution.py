import requests
from utils.CONFIG import API_KEY  # Assurez-vous que votre API_KEY est correctement importé

def get_city_coordinates(city_name):
    # URL pour l'API de géocodage
    url_geo_coding = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}"

    # Faire la requête HTTP
    response = requests.get(url_geo_coding)
    
    if response.status_code == 200:
        data = response.json()
        
        # Si nous avons des résultats
        if data:
            # Afficher les données pour vérification
            print("Données géocodage obtenues :")
            print(data)
            
            # Extraire la latitude et longitude du premier résultat
            first_result = data[0]  # On suppose que la ville souhaitée est le premier résultat
            city_name_from_response = first_result.get('name')
            
            if city_name_from_response.lower() == city_name.lower():
                lat = first_result.get('lat')
                lon = first_result.get('lon')
                return lat, lon
            else:
                print(f"La ville {city_name} n'a pas été trouvée.")
                return None
        else:
            print("Aucun résultat trouvé pour la ville.")
            return None
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def get_airpollution(lat, lon):
    url_air_pollution = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    # Faire la requête HTTP
    response = requests.get(url_air_pollution)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    city_name = "Paris"  # Nom de la ville à rechercher
    
    coordinates = get_city_coordinates(city_name)
    
    if coordinates:
        lat, lon = coordinates
        print(f"Coordonnées pour {city_name}: Latitude = {lat}, Longitude = {lon}")
        
        airpollution = get_airpollution(lat, lon)
        
        if airpollution:
            print("Données sur la pollution de l'air :")
            for key, value in airpollution.items():
                print(f"{key}: {value}")
        else:
            print("Échec de la récupération des données sur la pollution de l'air.")
    else:
        print("Échec de la récupération des coordonnées.")
