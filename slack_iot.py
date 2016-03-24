from slackclient import SlackClient
import urllib.request
import pywapi

token = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
sc = SlackClient(token)

print(sc.rtm_connect())

city = "Miskolc"

while True:
    new_evts = sc.rtm_read()
    for evt in new_evts:
      print(evt)
      if "type" in evt:
        if evt["type"] == "message" and "text" in evt:
          message=evt["text"]
          str_message = str(message)

          splitted_message = []
          splitted_message = str_message.split('_')

          try:
              print(splitted_message[1])
          except:
              print("Except")

          if (splitted_message[0] == "#weather" and len(splitted_message) > 1):
              try:
                  city = splitted_message[1]
                  lookup = pywapi.get_location_ids(city)

                  for i in lookup:
                    location_id = i

                  weather_com_result = pywapi.get_weather_from_weather_com(location_id)

                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in " + city + ".",
                    username='codecool_bot', icon_emoji=':cc:'))
              except:
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Something wrong... Sorry :( :weary: :no_entry:",
                    username='codecool_bot', icon_emoji=':cc:'))

          elif (splitted_message[0] == "#weather"):
              try:
                  lookup = pywapi.get_location_ids("Miskolc")

                  for i in lookup:
                    location_id = i

                  weather_com_result = pywapi.get_weather_from_weather_com(location_id)

                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in " + city + ".",
                    username='codecool_bot', icon_emoji=':cc:'))
              except:
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Something wrong... Sorry :( :weary: :no_entry:",
                    username='codecool_bot', icon_emoji=':cc:'))

          elif (message == "#make_coffee_now" ):
              try:
                  urllib.request.urlopen("http://192.168.150.175:8081/?lighton").read()
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="10perc és kész! ;) :coffee:",
                    username='codecool_bot', icon_emoji=':cc:'))
              except:
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Something wrong... Sorry :( :weary: :no_entry:",
                    username='codecool_bot', icon_emoji=':cc:'))

          elif (message == "#stop_make_coffee" ):
              try:
                  urllib.request.urlopen("http://192.168.150.175:8081/?lightoff").read()
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="I stopped to make coffee :) :x:",
                    username='codecool_bot', icon_emoji=':cc:'))
              except:
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Something wrong... Sorry :( :weary: :no_entry:",
                    username='codecool_bot', icon_emoji=':cc:'))

          elif (message == "#weather" ):
              try:
                  lookup = pywapi.get_location_ids(city)

                  for i in lookup:
                    location_id = i

                  weather_com_result = pywapi.get_weather_from_weather_com(location_id)

                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in " + city + ".",
                    username='codecool_bot', icon_emoji=':cc:'))
              except:
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Something wrong... Sorry :( :weary: :no_entry:",
                    username='codecool_bot', icon_emoji=':cc:'))
