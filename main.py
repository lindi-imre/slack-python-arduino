from slackclient import SlackClient

TOKEN = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
SC = SlackClient(TOKEN)
CC_LOGO = ":cc:"

print(SC.rtm_connect())


def help_msg():
    return SC.api_call(
        "chat.postMessage", channel="#test", text="Command list: \n"
                                                  "#authors - Writes out authors \n"
                                                  "#todo_add: something - Adds a todo element \n"
                                                  "#todo_del: something - Removes your todo element \n"
                                                  "#todo - Writes out your todo list \n"
                                                  "#weather - Writes out current weather \n"
                                                  "#make_coffee - Turn on the coffee machine ;) \n"
                                                  "#stop_coffee - Turn off the coffee machine",
        username='codecool_bot', icon_emoji=CC_LOGO)


def authors_msg():
    return SC.api_call(
                    "chat.postMessage", channel="#test", text="Kristof Bodnar, Imre Lindi, David Levai",
                    username='codecool_bot', icon_emoji=CC_LOGO)


def do_something(message: str):
    if message == "#help":
        print(help_msg())
    elif message == "#authors":
        print(authors_msg())


while True:
    new_evts = SC.rtm_read()
    for evt in new_evts:
        print(evt)
        if "type" in evt:
            if evt["type"] == "message" and "text" in evt:
                message = evt["text"]
                do_something(message)
