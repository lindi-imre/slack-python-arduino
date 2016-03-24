from slackclient import SlackClient

TOKEN = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
SC = SlackClient(TOKEN)

print(SC.rtm_connect())

music_dict = {"Leo Moracchioli - Beat It metal cover": "https://www.youtube.com/watch?v=EN6nLcix45U",
              "Elena Feat. Glance - Mamma Mia (He's Italiano) (Bodybangers Remix)": "https://www.youtube.com/watch?v=ohj_GU59UF8"}

while True:
    new_evts = SC.rtm_read()
    for evt in new_evts:
        print(evt)
        if "type" in evt:
            if evt["type"] == "message" and "text" in evt:
                message = evt["text"]
                if message == "#some_music":
                    for k, v in music_dict.items():
                        print(SC.api_call(
                        "chat.postMessage", channel="#test", text=k + v,
                        username='codecool_bot'))
