from plugins import Robot


def handle(message):
    message = message
    print(message)
    Robot().say(acceptwxid='wxid_5mqujdbpxfrv22', msg="nihao")
