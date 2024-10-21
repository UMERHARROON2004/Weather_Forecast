import requests
api_key = "Enter your openWeathermap API key"
while True:
    city_name = input("Enter your City name (or press 'q' to quit)\n")
    if city_name.lower() == 'q':
        print("------Exiting the program-------")
        print("Exit")
        break
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Weather is: ", data['weather'][0]['description'])
        print("Current Temperature is: ", data['main']['temp'])
        print("Current Temperature Feels Like is: ", data['main']['feels_like'])
        print("Current Humidity is: ", data['main']['humidity'])
    else:
        print("Error:", response.status_code, response.text)


