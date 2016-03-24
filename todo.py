from slackclient import SlackClient

token = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
sc = SlackClient(token)

print(sc.rtm_connect())

todo_list = []

while True:
    new_evts = sc.rtm_read()
    for evt in new_evts:
        print(evt)
        if "type" in evt:
            if evt["type"] == "message" and "text" in evt:
                message = evt["text"]
                if message.startswith("#todo_add: "):
                    todo_list.append(message[10:])
                    print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Added to TO-DO list: " + message[10:],
                    username='codecool_bot'))
                if message.startswith("#todo_del: "):
                    todo_list.remove(message[10:])
                    print(sc.api_call(
                    "chat.postMessage", channel="#test", text="Removed from TO-DO list: " + message[10:],
                    username='codecool_bot'))
                if message == "#todolist":
                    print(sc.api_call(
                    "chat.postMessage", channel="#test", text=todo_list,
                    username='codecool_bot'))
