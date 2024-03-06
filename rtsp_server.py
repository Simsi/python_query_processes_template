import multiprocessing
import numpy as np
import time


class RTSPServer(multiprocessing.Process):
    def __init__(self, queue: multiprocessing.Queue):
        super().__init__()

        # TODO init everything needed

        self.queue = queue

        self._target = self.host_server 


    def host_server(self):
        while True:
            if self.queue.qsize() > 0:
                data = self.queue.get()
                print(f"\nReceived {data}!")

    
    def put(self, data: any):
        self.queue.put(data)


    def get_queue_len(self):
        return self.queue.qsize()