import multiprocessing
import numpy as np
import time


class Template(multiprocessing.Process):
    def __init__(self, queue: multiprocessing.Queue):
        super().__init__()

        # TODO init everything needed

        self.queue = queue

        self._target = self.your_target_function


    def your_target_function(self):
        while True:
            # Do sth
            data = np.random.randint(10)
            self.queue.put(data)


    def get(self):
        if self.queue.qsize() > 0:
            return self.queue.get()
        else:
            return None


    def put(self, data):
        self.queue.put(data)


    def get_queue_len(self):
        return self.queue.qsize()