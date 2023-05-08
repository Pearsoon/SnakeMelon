import json
import requests

with open("config.json", "r") as f:
    config = json.loads(f.read())
    print(config)


class QL:
    address = config.get("address")
    print(address)
    id = config.get("clint_id")
    secret = config.get("clint_secret")

    def __init__(self):
        """
        初始化
        """
        self.valid = True
        self.login()

    def print_log(self, content: str) -> None:
        """
        日志
        """
        print(content)

    def login(self) -> None:
        """
        登录
        """
        url = f"{self.address}open/auth/token?client_id={self.id}&client_secret={self.secret}"
        try:
            response = requests.get(url).json()
            if response['code'] == 200:
                self.auth = f"{response['data']['token_type']} {response['data']['token']}"
            else:
                self.print_log(f"登录失败：{response['message']}")
        except Exception as e:
            self.valid = False
            self.print_log(f"登录失败：{str(e)}")

    def get_envs(self) -> list:
        """获取环境变量"""
        url = f"{self.address}open/envs"
        headers = {"Authorization": self.auth}
        try:
            response = requests.get(url, headers=headers).json()
            if response['code'] == 200:
                return response['data']
            else:
                self.print_log(f"获取环境变量失败：{response['message']}")
        except Exception as e:
            self.print_log(f"获取环境变量失败：{str(e)}")

    def add_envs(self, envs: list) -> bool:
        """
        新建环境变量
        [{"value": "变量值",
        "name": "变量名",
        "remarks": "备注" }]
        """
        url = f"{self.address}open/envs"
        headers = {"Authorization": self.auth, "content-type": "application/json"}
        try:
            response = requests.post(url, headers=headers, data=json.dumps(envs)).json()
            if response['code'] == 200:
                self.print_log(f"新建环境变量成功：{len(envs)}")
                return True
            else:
                self.print_log(f"新建环境变量失败：{response['message']}")
                return False
        except Exception as e:
            self.print_log(f"新建环境变量失败：{str(e)}")
            return False

    def update_env(self, env: dict) -> bool:
        """
        更新环境变量
        {"value": "变量值",
        "name": "变量名",
         "remarks": "备注",
         "id": 0 }
        """
        url = f"{self.address}open/envs"
        headers = {"Authorization": self.auth, "content-type": "application/json"}
        try:
            response = requests.put(url, headers=headers, data=json.dumps(env)).json()
            if response['code'] == 200:
                self.print_log(f"更新环境变量成功")
                return True
            else:
                self.print_log(f"更新环境变量失败：{response['message']}")
                return False
        except Exception as e:
            self.print_log(f"更新环境变量失败：{str(e)}")
            return False

    def delete_envs(self, ids: list) -> bool:
        """
        删除环境变量["RKuOUm0IR2HVpS5f"]
        """
        url = f"{self.address}open/envs"
        headers = {"Authorization": self.auth, "content-type": "application/json"}
        try:
            response = requests.delete(url, headers=headers, data=json.dumps(ids)).json()
            if response['code'] == 200:
                self.print_log(f"删除环境变量成功：{len(ids)}")
                return True
            else:
                self.print_log(f"删除环境变量失败：{response['message']}")
                return False
        except Exception as e:
            self.print_log(f"删除环境变量失败：{str(e)}")
            return False
