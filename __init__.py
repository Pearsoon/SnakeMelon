import information
from plugins import Robot
from plugins import greeting

if __name__ == '__main__':
    q = information.run()
    Robot = Robot()
    print(Robot.url)
    Robot.add_plugin(plugin=greeting)
    print(Robot.plugins)

    while True:
        message = q.get()
        Robot.handle_message(message=message)
