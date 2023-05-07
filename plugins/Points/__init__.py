import json


class Points:
    path = "plugins\\Points\\data.json"

    def __int__(self, path):
        self.path = path

    def read_points(self, name):
        """读取积分"""
        with open(self.path, 'r') as f:
            data = json.load(f)
            points = data.get(name, 0)
        return points

    def write_points(self, name, points):
        """更新积分"""
        with open(self.path, 'r') as f:
            data = json.load(f)
        data[name] = points
        with open(self.path, 'w') as f:
            json.dump(data, f)

    def add_points(self, name, points):
        """加减积分"""
        with open(self.path, 'r') as f:
            data = json.load(f)
            current_points = data.get(name, 0)
            current_points += points
            data[name] = current_points
        with open(self.path, 'w') as f:
            json.dump(data, f)
