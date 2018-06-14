#!/usr/bin/python3
import threading
import time

import cv2
import _thread
from time import sleep
from Recognition.Recognition import Recognition
from videoStream import _try
from ps_drone.ps_drone import Drone as psDrone


class ImageProcessingThread(threading.Thread):

    def __init__(self, threadID, name, drone):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name = name
        self.recognition = Recognition(threshold=0.2)
        self.drone = drone

    def run(self):
        _try(self.process_image)

    def process_image(self, image):
        # print("Processing image.")

        height, width, _ = image.shape

        result = self.recognition.recognize(image)

        for qr in filter(lambda x: x['label'] == 'qr', result):
            print(qr, height, width)
            top_left = qr['topleft']

            closeness_x = width / 2 / top_left['x']
            print("closeness:" + str(closeness_x))

            if closeness_x > 1.1:
                drone.left()
            elif closeness_x < 0.9:
                drone.right()
            else:
                drone.hover()

            continue  # exit after first qr.


class Drone:
    """
    Decorator for ps drone
    """

    def __init__(self, demo=False):
        self.drone = psDrone()
        self.drone.startup()
        print(self.drone.getBattery())
        self.recognition = Recognition(threshold=0.2)
        self.demo = demo

    def take_off(self):
        print("take off")
        if not self.demo:
            self.drone.takeoff()  # Drone starts
            sleep(7.5)
            self.drone.hover()

    def hover(self):
        if not self.demo:
            self.drone.stop()
        print("hover")

    def land(self):
        if not self.demo:
            self.drone.land()
        print("land")

    def search(self):
        if not self.demo:
            self.drone.turnLeft(60)
        print("search")

    def forward(self):
        if not self.demo:
            self.drone.moveForward(0.1)
        print("forward")

    def rotate_left(self, wait=0.1):
        print("rotate left")
        if not self.demo:
            self.drone.turnLeft()
            sleep(wait)
            self.hover()

    def rotate_right(self, wait=0.1):
        print("rotate eight")
        if not self.demo:
            self.drone.turnRight()
            sleep(wait)
            self.hover()

    def left(self, wait=0.3):
        if not self.demo:
            self.drone.moveLeft(0.1)
            sleep(wait)
            self.hover()
        print("left")

    def right(self, wait=0.3):
        if not self.demo:
            self.drone.moveRight(0.1)
            sleep(wait)
            self.hover()
        print("right")

    def process_image(self, image):
        print("Processing image.")

        height, width, _ = image.shape

        startTime = time.time()
        result = self.recognition.recognize(image)

        elapsedTime = time.time() - startTime
        print("took: " + str(elapsedTime))

        for qr in filter(lambda x: x['label'] == 'qr', result):
            print(qr, height, width)
            top_left = qr['topleft']

            closeness_x = width / 2 / (top_left['x']+1)
            print("closeness:" + str(closeness_x))

            if closeness_x > 1.15:
                drone.rotate_left()
            elif closeness_x < 0.85:
                drone.rotate_right()
            else:
                drone.hover()

            continue  # exit after first qr.


if __name__ == '__main__':
    drone = Drone(demo=True)
    drone.take_off()
    _try(drone.process_image)

    # thread = ImageProcessingThread(1, "Thread-1", drone)
    # thread.start()

    input("Press Enter to continue...")

    drone.land()
