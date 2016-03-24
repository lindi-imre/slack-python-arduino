from slackclient import SlackClient

token = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
sc = SlackClient(token)

print(sc.rtm_connect())

while True:
    new_evts = sc.rtm_read()
    for evt in new_evts:
        print(evt)
        if "type" in evt:
            if evt["type"] == "message" and "text" in evt:
                message = evt["text"]
                if message == "#help":
                    print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Commandlist: \n"
                                                              "#authors - Writes out authors \n"
                                                              "#todo_add: something - Adds a todo element \n"
                                                              "#todo_del: something - Removes your todo element \n"
                                                              "#todo - Writes out your todo list \n"
                                                              "#weather - Writes out current weather \n"
                                                              "#make_coffee - Turn on the coffe machine ;) \n"
                                                              "#stop_coffee - Turn off the coffe machine",
                                                              username='codecool_bot'))
