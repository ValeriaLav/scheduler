import threading as t

lock = t.Lock()


class Logger():
    def __init__(self):
        lock = t.Lock()
        pass
    def Write(self):

        with lock:
            pass