from plugins import Robot


def handle(msg):
    if msg["content"]["msg"] == "help":
        wxid = msg["content"]["from_wxid"]
        print("help")
        Robot().say(to_wxid=wxid,msg="******")

