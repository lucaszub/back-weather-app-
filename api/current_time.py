from fastapi import APIRouter
from openweathermap.currentime import get_actual_weather

router = APIRouter()

@router.get("/")
async def get_weather(city: str):

    actual = get_actual_weather(city)
    

    return {"meteo actuelle": actual}

