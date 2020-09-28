import threading


class RunInThread(object):
    def __init__(self, func: callable, *args):
        thread = threading.Thread(target=func, args=(i for i in args))
        thread.start()
