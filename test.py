import cv2

from Recognition.Recognition import Recognition

if __name__ == '__main__':
    img = cv2.imread('examples/8.jpg')
    #img = Image.open('examples/7.jpg')
    recognition = Recognition(img)
    recognition.dd(img)
    print(recognition.recognize())
