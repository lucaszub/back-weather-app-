from fastapi import APIRouter
from openweathermap.airpollution import get_city_coordinates, get_airpollution

router = APIRouter()

@router.get("/")
async def get_pollution(city: str):

    coordinates = get_city_coordinates(city)
    if coordinates:
        lat, lon = coordinates

        data = get_airpollution(lat, lon)

        airpollution = data.get('list')



    

    return {"airpollution": airpollution}

