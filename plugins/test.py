from plugins.QingLong import QL

QL = QL()


def handle(msg):
    meg = QL.get_envs()
    print(meg)
