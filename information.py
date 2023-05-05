from multiprocessing import Process, Queue


def accept_information(message_queue):
    # Flask 代码
    from flask import request, jsonify, Flask

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def del_device():
        message_queue.put(request.json)
        return "200"

    app.run()


def run():
    message_queue = Queue()
    p1 = Process(target=accept_information, args=(message_queue,))  # flask
    p1.start()  # flask
    return message_queue
