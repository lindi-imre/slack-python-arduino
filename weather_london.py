import pywapi

weather_com_result = pywapi.get_weather_from_weather_com('HUXX0015')

print("Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in Miskolc.")