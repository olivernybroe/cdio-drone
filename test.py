import cv2
import time

from PIL import Image

from Recognition.Recognition import Recognition

if __name__ == '__main__':
    img = cv2.imread('examples/7.jpg')
    #img = Image.open('examples/7.jpg')
    recognition = Recognition(img)
    print(recognition.recognize())
