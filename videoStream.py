import cv2
from time import sleep
import Recognition.Recognition


def _try():
    running = False
    while not running:
        print("Trying to connect.")
        cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
        running = cam.isOpened()
        sleep(0.1)

    while running:
        running, frame = cam.read()
        if running and frame is not None:
            _process_image(frame)

    print("Disconnected, reconnecting to drone.")
    _try()


def _process_image(image):
    #print(Recognition.Recognition.Recognition.recognize(image))
    Recognition.Recognition.Recognition.show(image)
    if cv2.waitKey(1) & 0xFF == 27:
        exit(0)


_try()
cv2.waitKey(0)
cv2.destroyAllWindows()


'''

running = True
while running:
    # get current frame of video
    running, frame = cam.read()
    if running:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            # escape key pressed
            running = False
    else:
        # error reading frame
        print('error reading video feed')
cam.release()
cv2.destroyAllWindows()
'''