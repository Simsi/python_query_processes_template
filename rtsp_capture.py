import multiprocessing
import numpy as np
import time


class RTSPCapture(multiprocessing.Process):
    def __init__(self, queue: multiprocessing.Queue):
        super().__init__()

        # TODO init everything needed

        self.queue = queue

        self._target = self.capture


    def capture(self):
        while True:
            data = np.random.randint(10)
            self.queue.put(data)
            #time.sleep(0.2)


    def get(self):
        if self.queue.qsize() > 0:
            return self.queue.get()
        else:
            return None


    def get_queue_len(self):
        return self.queue.qsize()