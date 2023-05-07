from plugins import Robot
from plugins.Points import Points

Robot = Robot()
Points = Points()


def handle(msg):
    print(msg)

    if msg["Event"] == "EventPrivateChat" and \
            msg["content"]["type"] == 2000:
        wxid = msg["content"]["from_wxid"]
        msg = Robot.change_msg(data=msg)
        payer_pay_id = msg["payer_pay_id"]
        receiver_pay_id = msg["receiver_pay_id"]
        paysubtype = msg["paysubtype"]
        money = msg["money"]
        Robot.accept_transfer(from_wxid=wxid, payer_pay_id=payer_pay_id, receiver_pay_id=receiver_pay_id,
                              paysubtype=paysubtype, money=money)
        points = eval(money) * 100
        Points.add_points(name=wxid, points=points)
        Robot.say(to_wxid=wxid, msg=f"收到您的砖帐,为您赠添∫{points}")
