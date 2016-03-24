# from slackclient import SlackClient
#
# token = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
# sc = SlackClient(token)
#
# print(sc.rtm_connect())
#
# while True:
#     new_evts = sc.rtm_read()
#     for evt in new_evts:
#         print(evt)
#         if "type" in evt:
#             if evt["type"] == "message" and "text" in evt:
#                 message = evt["text"]
#                 if message == "#authors":
#                     print(sc.api_call(
#                     "chat.postMessage", channel="#test", text="The one and only Imre Lindi! ",
#                     username='codecool_bot'))
