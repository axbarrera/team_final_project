rain =[]
for lat, lng in zip(cities_data['lat'],cities_data['lng']):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?lat={float(lat)}&lon={float(lng)}&APPID={api_key}"
    data = rq.get(base_url).json()
    try:
        rain.append(data["rain"]["1h"])
    except:
        rain.append(0)
    time.sleep(1.5)
    
pprint(rain)


cities_data.to_csv("california_cities_1h_rainfall")