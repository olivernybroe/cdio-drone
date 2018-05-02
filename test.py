import cv2
import time

from PIL import Image

from Recognition.Recognition import Recognition

if __name__ == '__main__':
    img = cv2.imread('examples/4.jpg', 0)
    recognition = Recognition(img)
    print(recognition.recognise())
