import multiprocessing
import numpy as np
import time


class NNInterractor(multiprocessing.Process):
    def __init__(self, in_queue: multiprocessing.Queue, out_queue: multiprocessing.Queue):
        super().__init__()

        # TODO init everything needed

        self.in_queue = in_queue
        self.out_queue = out_queue

        self._target = self.inference


    def inference(self):
        while True:
            if self.in_queue.qsize() > 0:
                data = self.in_queue.get()
                processed_data = self.process_data(data)
                self.out_queue.put(processed_data)


    def process_data(self, data):
        time.sleep(0.25)
        processed_data = data * 10
        return processed_data
    

    def put(self, data: any):
        self.in_queue.put(data)


    def get(self):
        if self.out_queue.qsize() > 0:
            return self.out_queue.get()
        else:
            return None


    def get_in_queue_len(self):
        return self.in_queue.qsize()
    

    def get_out_queue_len(self):
        return self.out_queue.qsize()
