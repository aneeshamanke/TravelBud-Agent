import requests
import os

WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url=f"http://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city,
        "aapid":WEATHER_API_KEY,
        "units":"metric"
    }
    
    response=requests.get(url,params=params)
    if response.status_code==200:
        data=response.json()
        desc=data['weather'][0]['description'].capitalize()
        temp=data['main']['temp']
        
        return f"{city.title()}:{desc},{temp}c"
    else:
        return f"weather for the {city} not found"
    
    
