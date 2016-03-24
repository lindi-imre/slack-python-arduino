from slackclient import SlackClient
import urllib.request

token = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
sc = SlackClient(token)

print(sc.rtm_connect())

while True:
    new_evts = sc.rtm_read()
    for evt in new_evts:
      print(evt)
      if "type" in evt:
        if evt["type"] == "message" and "text" in evt:
          message=evt["text"]
          if (evt['text'] == "#make_coffee_now" ):
              try:
                  urllib.request.urlopen("http://192.168.150.175:8081/?lighton").read()
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="10perc és kész! ;) :coffee:",
                    username='codecool_bot', icon_emoji=':coffee:'))
              except:
                  print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Something wrong... Sorry :( :weary: :no_entry:",
                    username='codecool_bot', icon_emoji=':no_entry:'))
