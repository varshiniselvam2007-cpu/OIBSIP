import requests

city = input("Enter city name: ").strip()

if city == "":
    print("Error: City name cannot be empty.")
else:
    api_key = "0f2125dd70993b7a721779524a85206e"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp_c = data["main"]["temp"]
            temp_f = (temp_c * 9/5) + 32
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            print("\nWeather Details")
            print("City:", city)
            print("Temperature:", round(temp_c, 2), "°C")
            print("Temperature:", round(temp_f, 2), "°F")
            print("Humidity:", humidity, "%")
            print("Weather:", weather)
            print("Wind Speed:", wind, "m/s")
        else:
            print("Error:", data.get("message", "City not found"))

    except requests.exceptions.RequestException:
        print("Network Error. Please try again.")
