import requests

def get_weather(city):
    API_KEY = "5d17b07f534f8fa0df068fb998b792f6"  
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,         
        "appid": API_KEY, 
        "units": "metric"  
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description'].title()
        
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    else:
        print(" City not found or API request failed.")  
        
get_weather("rajkot")
