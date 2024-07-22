from fastapi import APIRouter
from openweathermap.forecast_4_day import get_forecast_weather

router = APIRouter()

@router.get("/")
async def get_prediction(city: str):

    prediction = get_forecast_weather(city)
    

    return {"prediction meteo": prediction}