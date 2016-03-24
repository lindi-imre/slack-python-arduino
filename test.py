import time
from slackclient import SlackClient

token = "xoxb-29046773986-BphYFCMFDm4ZmpnrwyJln2qm"
sc = SlackClient(token)
print(sc.api_call("api.test"))
print(sc.api_call("channels.info", channel="C0V325QA3"))
#print(sc.api_call(
#    "chat.postMessage", channel="#test", text="I don't asdasd!!!!! :stars:",
#    username='gutyul_testbot', icon_emoji=':robot_face:'
#))

print(sc.rtm_connect())
print(sc.rtm_read())
