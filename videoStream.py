import _thread
import threading

import cv2
from time import sleep


def _try(process_image):
    running = False
    while not running:
        print("Trying to connect.")
        cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
        cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        running = cam.isOpened()
        sleep(0.1)

    print("Connected.")
    count = 0
    while running:
        running, frame = cam.read()

        if running and frame is not None and (count/6) % 2 == 0:
            process_image(frame)
            # _thread.start_new_thread(process_image, (frame,))

        count = count+1

    print("Disconnected, reconnecting to drone.")
    _try(process_image)
