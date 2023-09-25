import requests, json # importing requests and json
BASE_URL = https://api.openweathermap.org/data/2.5/weather? # base URL
CITY = "Hyderabad"

# API key API_KEY = "Your API Key"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY # upadting the URL
response = requests.get(URL) # HTTP request
if response.status_code == 200: # checking the status code of the request
data = response.json() # getting data in the json format
main = data['main'] # getting the main dict block
temperature = main['temp'] # getting temperature
humidity = main['humidity'] # getting the humidity
pressure = main['pressure'] # getting the pressure
report = data['weather'] # weather report
print(f"{CITY:-^30}")
print(f"Temperature: {temperature}")
print(f"Humidity: {humidity}")
print(f"Pressure: {pressure}")
print(f"Weather Report: {report[0]['description']}")
else:
print("Error in the HTTP request") 
