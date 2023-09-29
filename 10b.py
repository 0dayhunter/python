import requests, json  # importing requests and json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # base URL
CITY = "Bangalore"
API_KEY = "6f4ba13edf60f5338d0078eb0717ae85"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY  # updating the URL

response = requests.get(URL)  # HTTP request

if response.status_code == 200:  # checking the status code of the request
    data = response.json()  # getting data in the json format
    main = data['main']  # getting the main dict block
    temperature = main['temp']  # getting temperature
    humidity = main['humidity']  # getting the humidity
    pressure = main['pressure']  # getting the pressure
    report = data['weather'][0]['description']  # weather report

    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report}")
else:
    print("Error in the HTTP request")
