import time


class Time():
    def __init__(self):
        self.total_time = time.time()
        self.start()

    def start(self):
        self.time = time.time()

    def end(self, message='end:'):
        elapsed_time = time.time() - self.time
        print('{} {:.5f}'.format(message, elapsed_time))

    def continued(self, message='end:'):
        self.end(message)
        self.start()

    def show_total(self):
        elapsed_time = time.time() - self.total_time
        print('{} {:.5f}'.format('total:', elapsed_time))
