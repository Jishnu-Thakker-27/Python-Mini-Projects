import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("WEATHER_API_KEY")

place=input("Enter the location: ")
response=requests.get(url=f"http://api.weatherstack.com/current?access_key={api_key}&query={place}")

data=response.json()

print(f"Location: {data["location"]["name"]},{data["location"]["region"]},{data["location"]["country"]}")
print(f"Time: {data["location"]["localtime"]}")
print(f"Temperature: {data["current"]["temperature"]} degree Celcius")
