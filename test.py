#!/usr/bin/python3
import threading

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
        #print("Processing image.")
        cv2.imshow("image", image)

        height, width, _ = image.shape

        result = self.recognition.recognize(image)

        for qr in filter(lambda x: x['label'] == 'qr', result):
            print(qr, height, width)
            top_left = qr['topleft']

            closeness_x = width/2/top_left['x']
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

    def __init__(self):
        self.drone = psDrone()
        # self.drone.startup()

    def take_off(self):
        print("take off")
        # self.drone.takeoff()  # Drone starts
        # sleep(7.5)
        # self.drone.hover()

    def hover(self):
        #self.drone.stop()
        print("hover")

    def land(self):
        #self.drone.land()
        print("land")

    def search(self):
        #self.drone.turnLeft(60)
        print("search")

    def forward(self):
        #self.drone.moveForward(0.1)
        print("forward")

    def left(self):
        #self.drone.moveLeft(0.1)
        print("left")

    def right(self):
        #self.drone.moveRight(0.1)
        print("right")


if __name__ == '__main__':
    #cv2.namedWindow('drone')

    drone = Drone()

    drone.take_off()

    thread = ImageProcessingThread(1, "Thread-1", drone)
    thread.start()

    input("Press Enter to continue...")

    drone.land()
