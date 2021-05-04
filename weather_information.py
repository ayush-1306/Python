import requests
city = input("Enter City Name ")
base_url = "http://api.openweathermap.org/data/2.5/weather?q="
api_key = "Enter your API key"  
url = base_url+city+"&appid="+api_key
response = requests.get(url)
x = response.json()
if x['cod'] != 404:
    print("City Name : ", x['name'])
    print("Weather : ", x["weather"][0]['main'])
    print("Temperature : ", round(x['main']['temp'] - 273.15,2))
    print("Maximum Temperature : ", round(x['main']['temp_max'] - 273.15,2))
    print("Minimum Temperature : ", round(x['main']['temp_min'] - 273.15,2))
else:
    print("City Not Found")
