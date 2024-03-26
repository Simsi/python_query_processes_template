import multiprocessing
import numpy as np
import time

from rtsp_capture import RTSPCapture
from inference import NNInterractor
from rtsp_server import RTSPServer


class Pipeline():
    def __init__(self, queue_size=10):
        self.queue_size = queue_size

        self.capture_q = multiprocessing.Queue(maxsize=queue_size)
        self.in_inference_q = multiprocessing.Queue(maxsize=queue_size)
        self.out_inference_q = multiprocessing.Queue(maxsize=queue_size)
        self.server_q = multiprocessing.Queue(maxsize=queue_size)

        self.cap_node = RTSPCapture(queue=self.capture_q)
        self.inference_node = NNInterractor(in_queue=self.in_inference_q, out_queue=self.out_inference_q)
        self.server_node = RTSPServer(queue=self.server_q)

        self.cap_node.start()
        self.inference_node.start()
        self.server_node.start()


    def transfer_data(self):
        try:
            data = None
            inference_result = None
            if not self.capture_q.empty():
                data = self.capture_q.get()

            if data is not None and not self.in_inference_q.full():
                self.in_inference_q.put(data)

            if not self.out_inference_q.empty():
                inference_result = self.out_inference_q.get()

            if inference_result is not None and not self.server_q.full():
                self.server_q.put(inference_result)
        
        except Exception as e:
            print(str(e))


    def show_all_qsizes(self):
        print(
              f"\n Capture queue: {self.cap_node.queue.qsize()} \
              \n Inference in queue: {self.inference_node.in_queue.qsize()}\
              \n Inference out queue: {self.inference_node.out_queue.qsize()}\
              \n Server queue: {self.server_node.queue.qsize()}"
              )



def main():
    dz_detector = Pipeline()
    while True:
        dz_detector.show_all_qsizes()
        dz_detector.transfer_data()


if __name__ == "__main__":
    main()
