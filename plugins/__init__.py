import requests
import json

with open("config.json", "r") as f:
    config = json.loads(f.read())


class Robot:
    """定义一个robot的类"""
    plugins = []
    url = config.get("url")
    token = config.get("token")
    wxid = config.get("wxid")

    def __int__(self, url, token, wxid):
        self.url = url
        self.token = token
        self.wxid = wxid

    def add_plugin(self, plugin):
        """添加插件方法"""
        self.plugins.append(plugin)

    def handle_message(self, message):
        """处理消息的函数,用于将消息传入小插件中"""
        for plugin in self.plugins:
            print(plugin)
            plugin.handle(message=message)

    def post_(self, data_):
        """post函数,用于触发事件"""
        url = self.url
        response = requests.post(url=url, json=data_)
        return response

    def say(self, acceptwxid, msg):
        api_ = "SendTextMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{acceptwxid}",
            "msg": f"{msg}"
        }
        return self.post_(data_)
